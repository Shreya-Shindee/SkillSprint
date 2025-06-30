"""
Gamified Dashboard Router - Handles user stats, streaks, leaderboards, and achievements
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from typing import List, Dict, Any
from datetime import datetime, timedelta
from pydantic import BaseModel

from database.database import get_db
from models.models import User, XPTransaction, SkillProgress, QuizAttempt, UserBehavior, SubskillProgress
from utils.auth import get_current_active_user
from utils.adaptive_learning import adaptive_engine

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

# Response models
class DashboardStats(BaseModel):
    total_xp: int
    current_streak: int
    longest_streak: int
    skills_completed: int
    skills_in_progress: int
    total_study_time_minutes: int
    quiz_average_score: float
    weekly_xp: int
    daily_goal_completion: bool

class LeaderboardEntry(BaseModel):
    rank: int
    username: str
    total_xp: int
    current_streak: int
    skills_completed: int

class Achievement(BaseModel):
    id: str
    name: str
    description: str
    icon: str
    unlocked: bool
    unlocked_at: str = None
    progress: int = 0
    target: int = 1

@router.get("/stats", response_model=DashboardStats)
async def get_dashboard_stats(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Get comprehensive dashboard statistics for the current user
    """
    try:
        # Basic stats from user model
        total_xp = current_user.total_xp or 0
        current_streak = current_user.current_streak or 0
        longest_streak = current_user.longest_streak or 0
        
        # Skill progress stats
        skill_progress = db.query(SkillProgress).filter(
            SkillProgress.user_id == current_user.id
        ).all()
        
        skills_completed = len([sp for sp in skill_progress if sp.completed])
        skills_in_progress = len([sp for sp in skill_progress if not sp.completed and sp.progress_percentage > 0])
        
        # Study time from subskill progress
        total_study_time = db.query(func.sum(SubskillProgress.time_spent_minutes)).filter(
            SubskillProgress.user_id == current_user.id
        ).scalar() or 0
        
        # Quiz statistics
        quiz_attempts = db.query(QuizAttempt).filter(
            QuizAttempt.user_id == current_user.id
        ).all()
        
        quiz_average_score = 0
        if quiz_attempts:
            total_score = sum(attempt.score / attempt.total_questions for attempt in quiz_attempts)
            quiz_average_score = (total_score / len(quiz_attempts)) * 100
        
        # Weekly XP (last 7 days)
        week_ago = datetime.utcnow() - timedelta(days=7)
        weekly_xp = db.query(func.sum(XPTransaction.amount)).filter(
            XPTransaction.user_id == current_user.id,
            XPTransaction.created_at >= week_ago
        ).scalar() or 0
        
        # Daily goal completion (at least one subskill completed today)
        today = datetime.now().date()
        today_activity = db.query(UserBehavior).filter(
            UserBehavior.user_id == current_user.id,
            UserBehavior.timestamp >= datetime.combine(today, datetime.min.time()),
            UserBehavior.action_type == "complete_subskill"
        ).first()
        
        daily_goal_completion = bool(today_activity)
        
        return DashboardStats(
            total_xp=total_xp,
            current_streak=current_streak,
            longest_streak=longest_streak,
            skills_completed=skills_completed,
            skills_in_progress=skills_in_progress,
            total_study_time_minutes=int(total_study_time),
            quiz_average_score=round(quiz_average_score, 1),
            weekly_xp=weekly_xp,
            daily_goal_completion=daily_goal_completion
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get dashboard stats: {str(e)}"
        )

@router.get("/leaderboard", response_model=List[LeaderboardEntry])
async def get_leaderboard(
    limit: int = 10,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Get the XP leaderboard with user rankings
    """
    try:
        # Get top users by XP
        top_users = db.query(User).filter(
            User.is_active == True
        ).order_by(desc(User.total_xp)).limit(limit).all()
        
        leaderboard = []
        for rank, user in enumerate(top_users, 1):
            # Get skills completed for each user
            skills_completed = db.query(func.count(SkillProgress.id)).filter(
                SkillProgress.user_id == user.id,
                SkillProgress.completed == True
            ).scalar() or 0
            
            leaderboard.append(LeaderboardEntry(
                rank=rank,
                username=user.username,
                total_xp=user.total_xp or 0,
                current_streak=user.current_streak or 0,
                skills_completed=skills_completed
            ))
        
        return leaderboard
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get leaderboard: {str(e)}"
        )

@router.get("/achievements", response_model=List[Achievement])
async def get_achievements(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Get user's achievements and progress towards unlocking new ones
    """
    try:
        # Get user stats for achievement calculation
        stats = await get_dashboard_stats(current_user, db)
        
        # Define achievements
        achievements_definitions = [
            {
                "id": "first_steps",
                "name": "First Steps",
                "description": "Complete your first subskill",
                "icon": "🎯",
                "target": 1,
                "current": len([sp for sp in db.query(SubskillProgress).filter(
                    SubskillProgress.user_id == current_user.id,
                    SubskillProgress.completed == True
                ).all()])
            },
            {
                "id": "quick_learner",
                "name": "Quick Learner",
                "description": "Complete 10 subskills",
                "icon": "⚡",
                "target": 10,
                "current": len([sp for sp in db.query(SubskillProgress).filter(
                    SubskillProgress.user_id == current_user.id,
                    SubskillProgress.completed == True
                ).all()])
            },
            {
                "id": "skill_master",
                "name": "Skill Master",
                "description": "Complete your first skill",
                "icon": "🏆",
                "target": 1,
                "current": stats.skills_completed
            },
            {
                "id": "dedicated_learner",
                "name": "Dedicated Learner",
                "description": "Maintain a 7-day learning streak",
                "icon": "🔥",
                "target": 7,
                "current": stats.current_streak
            },
            {
                "id": "streak_champion",
                "name": "Streak Champion",
                "description": "Maintain a 30-day learning streak",
                "icon": "👑",
                "target": 30,
                "current": stats.current_streak
            },
            {
                "id": "quiz_ace",
                "name": "Quiz Ace",
                "description": "Achieve 90% average quiz score",
                "icon": "🎓",
                "target": 90,
                "current": int(stats.quiz_average_score)
            },
            {
                "id": "xp_collector",
                "name": "XP Collector",
                "description": "Earn 1000 XP",
                "icon": "💎",
                "target": 1000,
                "current": stats.total_xp
            },
            {
                "id": "xp_legend",
                "name": "XP Legend",
                "description": "Earn 10000 XP",
                "icon": "🌟",
                "target": 10000,
                "current": stats.total_xp
            },
            {
                "id": "time_investor",
                "name": "Time Investor",
                "description": "Spend 10 hours learning",
                "icon": "⏰",
                "target": 600,  # 10 hours in minutes
                "current": stats.total_study_time_minutes
            },
            {
                "id": "knowledge_seeker",
                "name": "Knowledge Seeker",
                "description": "Complete 5 different skills",
                "icon": "📚",
                "target": 5,
                "current": stats.skills_completed
            }
        ]
        
        achievements = []
        for achievement_def in achievements_definitions:
            unlocked = achievement_def["current"] >= achievement_def["target"]
            
            # For unlocked achievements, try to get unlock date from user behavior
            unlocked_at = None
            if unlocked:
                # This is simplified - in a real system you'd track achievement unlock dates
                unlocked_at = datetime.utcnow().isoformat()
            
            achievements.append(Achievement(
                id=achievement_def["id"],
                name=achievement_def["name"],
                description=achievement_def["description"],
                icon=achievement_def["icon"],
                unlocked=unlocked,
                unlocked_at=unlocked_at,
                progress=min(achievement_def["current"], achievement_def["target"]),
                target=achievement_def["target"]
            ))
        
        return achievements
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get achievements: {str(e)}"
        )

@router.get("/activity-feed")
async def get_activity_feed(
    limit: int = 20,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Get recent learning activities for the dashboard
    """
    try:
        # Get recent user activities
        activities = db.query(UserBehavior).filter(
            UserBehavior.user_id == current_user.id
        ).order_by(UserBehavior.timestamp.desc()).limit(limit).all()
        
        # Get recent XP transactions
        xp_transactions = db.query(XPTransaction).filter(
            XPTransaction.user_id == current_user.id
        ).order_by(XPTransaction.created_at.desc()).limit(10).all()
        
        # Format activities
        activity_feed = []
        
        for activity in activities:
            if activity.action_type == "complete_subskill":
                activity_feed.append({
                    "type": "subskill_completed",
                    "message": f"Completed subskill: {activity.subskill_name}",
                    "timestamp": activity.timestamp.isoformat(),
                    "icon": "✅",
                    "metadata": activity.metadata
                })
            elif activity.action_type == "complete_quiz":
                score = activity.metadata.get("score", 0)
                total = activity.metadata.get("total_questions", 1)
                percentage = int((score / total) * 100)
                activity_feed.append({
                    "type": "quiz_completed",
                    "message": f"Completed quiz with {percentage}% score",
                    "timestamp": activity.timestamp.isoformat(),
                    "icon": "🎯",
                    "metadata": activity.metadata
                })
            elif activity.action_type == "start_quiz":
                activity_feed.append({
                    "type": "quiz_started",
                    "message": f"Started a quiz",
                    "timestamp": activity.timestamp.isoformat(),
                    "icon": "📝",
                    "metadata": activity.metadata
                })
        
        # Add XP transactions to feed
        for xp in xp_transactions[:5]:  # Limit XP transactions
            activity_feed.append({
                "type": "xp_earned",
                "message": f"Earned {xp.amount} XP: {xp.description}",
                "timestamp": xp.created_at.isoformat(),
                "icon": "⭐",
                "metadata": {"amount": xp.amount, "type": xp.transaction_type}
            })
        
        # Sort by timestamp
        activity_feed.sort(key=lambda x: x["timestamp"], reverse=True)
        
        return {"activities": activity_feed[:limit]}
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get activity feed: {str(e)}"
        )

@router.get("/learning-insights")
async def get_learning_insights(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Get AI-powered learning insights and recommendations
    """
    try:
        # Get behavior analysis
        behavior_analysis = adaptive_engine.analyze_user_behavior(current_user.id, db)
        
        # Get collaborative recommendations
        recommendations = adaptive_engine.get_collaborative_recommendations(
            user_id=current_user.id,
            db=db,
            limit=3
        )
        
        # Generate insights based on user data
        insights = []
        
        # Learning style insight
        learning_style = behavior_analysis.get("learning_style", "balanced")
        insights.append({
            "type": "learning_style",
            "title": f"Your Learning Style: {learning_style.title()}",
            "description": f"You prefer {learning_style} learning approaches. We'll tailor your resources accordingly.",
            "actionable": True,
            "action": "View personalized resources"
        })
        
        # Engagement pattern insight
        engagement = behavior_analysis.get("engagement_patterns", {})
        session_frequency = engagement.get("session_frequency", "medium")
        if session_frequency == "low":
            insights.append({
                "type": "engagement",
                "title": "Increase Learning Frequency",
                "description": "Try to practice more regularly to improve retention and build stronger habits.",
                "actionable": True,
                "action": "Set daily reminders"
            })
        
        # Difficulty insight
        preferred_difficulty = behavior_analysis.get("preferred_difficulty", "beginner")
        insights.append({
            "type": "difficulty",
            "title": f"Optimal Difficulty: {preferred_difficulty.title()}",
            "description": f"Your performance is best at {preferred_difficulty} level content.",
            "actionable": True,
            "action": "Adjust difficulty settings"
        })
        
        # Completion rate insight
        completion_rate = behavior_analysis.get("completion_rate", 0)
        if completion_rate < 0.7:
            insights.append({
                "type": "completion",
                "title": "Focus on Completing Skills",
                "description": "You have several skills in progress. Focus on completing them for better learning outcomes.",
                "actionable": True,
                "action": "View skills in progress"
            })
        
        return {
            "insights": insights,
            "recommendations": recommendations,
            "behavior_summary": {
                "learning_style": learning_style,
                "preferred_difficulty": preferred_difficulty,
                "session_frequency": session_frequency,
                "completion_rate": completion_rate
            }
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get learning insights: {str(e)}"
        )

@router.get("/progress-chart")
async def get_progress_chart(
    days: int = 30,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Get progress chart data for the dashboard
    """
    try:
        # Get XP data over time
        start_date = datetime.utcnow() - timedelta(days=days)
        
        xp_transactions = db.query(XPTransaction).filter(
            XPTransaction.user_id == current_user.id,
            XPTransaction.created_at >= start_date
        ).order_by(XPTransaction.created_at).all()
        
        # Group by day
        daily_xp = {}
        cumulative_xp = 0
        
        for transaction in xp_transactions:
            date_str = transaction.created_at.date().isoformat()
            if date_str not in daily_xp:
                daily_xp[date_str] = 0
            daily_xp[date_str] += transaction.amount
        
        # Create chart data
        chart_data = []
        for i in range(days):
            date = (datetime.utcnow() - timedelta(days=days-1-i)).date()
            date_str = date.isoformat()
            daily_amount = daily_xp.get(date_str, 0)
            cumulative_xp += daily_amount
            
            chart_data.append({
                "date": date_str,
                "daily_xp": daily_amount,
                "cumulative_xp": cumulative_xp
            })
        
        # Get activity count data
        activities = db.query(UserBehavior).filter(
            UserBehavior.user_id == current_user.id,
            UserBehavior.timestamp >= start_date,
            UserBehavior.action_type.in_(["complete_subskill", "complete_quiz"])
        ).all()
        
        daily_activities = {}
        for activity in activities:
            date_str = activity.timestamp.date().isoformat()
            if date_str not in daily_activities:
                daily_activities[date_str] = 0
            daily_activities[date_str] += 1
        
        # Add activity data to chart
        for data_point in chart_data:
            data_point["activities"] = daily_activities.get(data_point["date"], 0)
        
        return {
            "chart_data": chart_data,
            "summary": {
                "total_days": days,
                "total_xp_gained": sum(daily_xp.values()),
                "most_productive_day": max(daily_xp.items(), key=lambda x: x[1]) if daily_xp else None,
                "average_daily_xp": sum(daily_xp.values()) / len(daily_xp) if daily_xp else 0
            }
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get progress chart: {str(e)}"
        )
