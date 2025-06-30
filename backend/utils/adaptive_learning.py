"""
Adaptive Learning Engine - Data-Driven Learning Path Optimization
Handles user behavior analysis, collaborative filtering, and dynamic difficulty adjustment
"""

import numpy as np
from typing import List, Dict, Any, Tuple, Optional
from datetime import datetime, timedelta
from collections import defaultdict
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from database.database import get_db
from models.models import (
    User, Skill, SubskillProgress, UserBehavior, QuizAttempt, 
    SkillProgress, Resource, UserRecommendation
)
import logging

logger = logging.getLogger(__name__)

class AdaptiveLearningEngine:
    def __init__(self):
        self.min_data_points = 5  # Minimum interactions needed for personalization
        self.similarity_threshold = 0.7  # Threshold for finding similar users
        
    def analyze_user_behavior(self, user_id: int, db: Session) -> Dict[str, Any]:
        """
        Analyze user's learning behavior patterns
        
        Args:
            user_id: User to analyze
            db: Database session
            
        Returns:
            Dict containing behavior analysis and insights
        """
        try:
            # Get user's learning history
            behaviors = db.query(UserBehavior).filter(
                UserBehavior.user_id == user_id
            ).order_by(UserBehavior.timestamp.desc()).limit(100).all()
            
            # Get quiz performance
            quiz_attempts = db.query(QuizAttempt).filter(
                QuizAttempt.user_id == user_id
            ).order_by(QuizAttempt.completed_at.desc()).limit(20).all()
            
            # Get skill progress
            skill_progress = db.query(SkillProgress).filter(
                SkillProgress.user_id == user_id
            ).all()
            
            # Analyze patterns
            analysis = {
                "learning_style": self._determine_learning_style(behaviors),
                "preferred_difficulty": self._analyze_difficulty_preference(quiz_attempts),
                "engagement_patterns": self._analyze_engagement_patterns(behaviors),
                "completion_rate": self._calculate_completion_rate(skill_progress),
                "average_session_time": self._calculate_average_session_time(behaviors),
                "struggling_topics": self._identify_struggling_topics(quiz_attempts, skill_progress),
                "strengths": self._identify_strengths(quiz_attempts, skill_progress),
                "learning_pace": self._analyze_learning_pace(behaviors, skill_progress),
                "recommended_adjustments": []
            }
            
            # Generate recommendations
            analysis["recommended_adjustments"] = self._generate_behavior_recommendations(analysis)
            
            return analysis
            
        except Exception as e:
            logger.error(f"Error analyzing user behavior for user {user_id}: {str(e)}")
            return self._default_behavior_analysis()
    
    def get_collaborative_recommendations(self, user_id: int, db: Session, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Generate recommendations based on similar users' behavior
        
        Args:
            user_id: Target user
            db: Database session
            limit: Number of recommendations to return
            
        Returns:
            List of recommended skills/resources
        """
        try:
            # Find similar users
            similar_users = self._find_similar_users(user_id, db)
            
            if not similar_users:
                return self._get_popular_recommendations(db, limit)
            
            recommendations = []
            
            # Get skills that similar users have completed but target user hasn't
            target_user_skills = set(
                skill.skill_id for skill in db.query(SkillProgress).filter(
                    SkillProgress.user_id == user_id
                ).all()
            )
            
            # Collect skills from similar users
            skill_scores = defaultdict(float)
            
            for similar_user_id, similarity_score in similar_users:
                similar_user_skills = db.query(SkillProgress).filter(
                    SkillProgress.user_id == similar_user_id,
                    SkillProgress.completed == True
                ).all()
                
                for skill_progress in similar_user_skills:
                    if skill_progress.skill_id not in target_user_skills:
                        skill_scores[skill_progress.skill_id] += similarity_score * skill_progress.progress_percentage
            
            # Sort by score and get top recommendations
            sorted_skills = sorted(skill_scores.items(), key=lambda x: x[1], reverse=True)
            
            for skill_id, score in sorted_skills[:limit]:
                skill = db.query(Skill).filter(Skill.id == skill_id).first()
                if skill:
                    recommendations.append({
                        "type": "skill",
                        "item_id": skill_id,
                        "title": skill.name,
                        "description": skill.description,
                        "score": score,
                        "reason": f"Users with similar learning patterns completed this skill"
                    })
            
            return recommendations
            
        except Exception as e:
            logger.error(f"Error generating collaborative recommendations: {str(e)}")
            return self._get_popular_recommendations(db, limit)
    
    def adjust_difficulty_dynamically(self, user_id: int, skill_id: int, db: Session) -> Dict[str, Any]:
        """
        Adjust learning path difficulty based on user performance
        
        Args:
            user_id: User to adjust for
            skill_id: Skill being learned
            db: Database session
            
        Returns:
            Dict containing difficulty adjustments and recommendations
        """
        try:
            # Get recent quiz performance
            recent_quizzes = db.query(QuizAttempt).filter(
                QuizAttempt.user_id == user_id,
                QuizAttempt.skill_id == skill_id
            ).order_by(QuizAttempt.completed_at.desc()).limit(5).all()
            
            # Get subskill progress
            subskill_progress = db.query(SubskillProgress).filter(
                SubskillProgress.user_id == user_id,
                SubskillProgress.skill_id == skill_id
            ).all()
            
            if not recent_quizzes:
                return {"difficulty_level": "beginner", "adjustments": []}
            
            # Calculate performance metrics
            avg_score = np.mean([q.score / q.total_questions for q in recent_quizzes])
            score_trend = self._calculate_score_trend(recent_quizzes)
            completion_rate = len([sp for sp in subskill_progress if sp.completed]) / max(len(subskill_progress), 1)
            
            # Determine current difficulty level
            current_difficulty = self._determine_difficulty_level(avg_score, score_trend, completion_rate)
            
            # Generate specific adjustments
            adjustments = []
            
            if avg_score < 0.6 and score_trend < 0:
                adjustments.extend([
                    "Reduce quiz difficulty",
                    "Add more foundational resources",
                    "Increase practice exercises",
                    "Suggest review of previous topics"
                ])
            elif avg_score > 0.8 and score_trend > 0:
                adjustments.extend([
                    "Increase challenge level",
                    "Add advanced topics",
                    "Suggest projects or real-world applications",
                    "Introduce time-based challenges"
                ])
            elif completion_rate < 0.5:
                adjustments.extend([
                    "Break down complex topics into smaller steps",
                    "Add more interactive elements",
                    "Provide additional motivation and encouragement"
                ])
            
            # Update user's learning preferences
            self._update_user_preferences(user_id, current_difficulty, db)
            
            return {
                "difficulty_level": current_difficulty,
                "average_score": avg_score,
                "score_trend": score_trend,
                "completion_rate": completion_rate,
                "adjustments": adjustments,
                "recommended_next_steps": self._get_next_steps(user_id, skill_id, current_difficulty, db)
            }
            
        except Exception as e:
            logger.error(f"Error adjusting difficulty for user {user_id}, skill {skill_id}: {str(e)}")
            return {"difficulty_level": "beginner", "adjustments": ["Continue with current pace"]}
    
    def generate_personalized_learning_path(self, user_id: int, skill_id: int, db: Session) -> Dict[str, Any]:
        """
        Generate a personalized learning path based on user's behavior and preferences
        
        Args:
            user_id: Target user
            skill_id: Skill to create path for
            db: Database session
            
        Returns:
            Dict containing personalized learning path
        """
        try:
            # Get user behavior analysis
            behavior_analysis = self.analyze_user_behavior(user_id, db)
            
            # Get skill details
            skill = db.query(Skill).filter(Skill.id == skill_id).first()
            if not skill:
                raise ValueError(f"Skill {skill_id} not found")
            
            # Get user's current progress
            progress = db.query(SkillProgress).filter(
                SkillProgress.user_id == user_id,
                SkillProgress.skill_id == skill_id
            ).first()
            
            # Generate adaptive path
            learning_path = {
                "skill_id": skill_id,
                "skill_name": skill.name,
                "user_level": behavior_analysis["preferred_difficulty"],
                "estimated_completion_time": self._estimate_completion_time(
                    skill, behavior_analysis["learning_pace"]
                ),
                "personalized_subskills": [],
                "recommended_resources": [],
                "milestones": [],
                "adaptive_features": []
            }
            
            # Customize subskills based on user preferences
            if skill.subskills:
                for i, subskill in enumerate(skill.subskills):
                    is_completed = progress and subskill in progress.completed_subskills
                    
                    personalized_subskill = {
                        "name": subskill,
                        "order": i + 1,
                        "completed": is_completed,
                        "difficulty": self._adjust_subskill_difficulty(
                            subskill, behavior_analysis["preferred_difficulty"]
                        ),
                        "estimated_hours": self._estimate_subskill_time(
                            subskill, behavior_analysis["learning_pace"]
                        ),
                        "resources": self._get_personalized_resources(
                            subskill, behavior_analysis["learning_style"], db
                        ),
                        "practice_exercises": self._get_practice_exercises(subskill),
                        "quiz_enabled": not is_completed
                    }
                    
                    learning_path["personalized_subskills"].append(personalized_subskill)
            
            # Add adaptive features based on user behavior
            learning_path["adaptive_features"] = self._get_adaptive_features(behavior_analysis)
            
            # Set up milestones
            learning_path["milestones"] = self._create_milestones(learning_path["personalized_subskills"])
            
            return learning_path
            
        except Exception as e:
            logger.error(f"Error generating personalized path: {str(e)}")
            return self._fallback_learning_path(skill_id, db)
    
    def track_user_interaction(self, user_id: int, action_type: str, skill_id: int = None, 
                              subskill_name: str = None, resource_id: int = None, 
                              metadata: Dict = None, db: Session = None):
        """
        Track user interaction for behavior analysis
        
        Args:
            user_id: User performing the action
            action_type: Type of action (view_resource, complete_subskill, etc.)
            skill_id: Related skill (optional)
            subskill_name: Related subskill (optional)
            resource_id: Related resource (optional)
            metadata: Additional data (optional)
            db: Database session
        """
        if not db:
            db = next(get_db())
        
        try:
            behavior = UserBehavior(
                user_id=user_id,
                action_type=action_type,
                skill_id=skill_id,
                subskill_name=subskill_name,
                resource_id=resource_id,
                metadata=metadata or {}
            )
            
            db.add(behavior)
            db.commit()
            
            # Update user's last activity
            user = db.query(User).filter(User.id == user_id).first()
            if user:
                user.last_activity = datetime.utcnow()
                db.commit()
            
        except Exception as e:
            logger.error(f"Error tracking user interaction: {str(e)}")
            db.rollback()
    
    def _determine_learning_style(self, behaviors: List[UserBehavior]) -> str:
        """Determine user's preferred learning style based on their behavior"""
        if not behaviors:
            return "balanced"
        
        # Count different types of resource interactions
        resource_types = defaultdict(int)
        for behavior in behaviors:
            if behavior.action_type == "view_resource" and behavior.metadata:
                resource_type = behavior.metadata.get("resource_type")
                if resource_type:
                    resource_types[resource_type] += 1
        
        if not resource_types:
            return "balanced"
        
        # Determine preferred style
        total_interactions = sum(resource_types.values())
        video_ratio = resource_types.get("video", 0) / total_interactions
        article_ratio = resource_types.get("article", 0) / total_interactions
        code_ratio = resource_types.get("github", 0) / total_interactions
        
        if video_ratio > 0.5:
            return "visual"
        elif article_ratio > 0.5:
            return "reading"
        elif code_ratio > 0.4:
            return "hands-on"
        else:
            return "balanced"
    
    def _analyze_difficulty_preference(self, quiz_attempts: List[QuizAttempt]) -> str:
        """Analyze user's preferred difficulty level based on quiz performance"""
        if not quiz_attempts:
            return "beginner"
        
        # Get average performance on different difficulty levels
        difficulty_scores = defaultdict(list)
        
        for attempt in quiz_attempts:
            if attempt.questions_data:
                for question in attempt.questions_data:
                    difficulty = question.get("difficulty", "medium")
                    # This is simplified - in practice, you'd track individual question performance
                    score = attempt.score / attempt.total_questions
                    difficulty_scores[difficulty].append(score)
        
        # Find the difficulty where user performs best (60-80% range)
        optimal_difficulty = "beginner"
        target_score_range = (0.6, 0.8)
        
        for difficulty, scores in difficulty_scores.items():
            if scores:
                avg_score = np.mean(scores)
                if target_score_range[0] <= avg_score <= target_score_range[1]:
                    optimal_difficulty = difficulty
                    break
        
        return optimal_difficulty
    
    def _analyze_engagement_patterns(self, behaviors: List[UserBehavior]) -> Dict[str, Any]:
        """Analyze when and how user engages with the platform"""
        if not behaviors:
            return {"peak_hours": [], "session_frequency": "low", "preferred_days": []}
        
        # Analyze time patterns
        hours = [behavior.timestamp.hour for behavior in behaviors]
        peak_hours = self._find_peak_hours(hours)
        
        # Analyze frequency
        dates = [behavior.timestamp.date() for behavior in behaviors]
        unique_dates = len(set(dates))
        days_span = (max(dates) - min(dates)).days if len(set(dates)) > 1 else 1
        session_frequency = "high" if unique_dates / max(days_span, 1) > 0.5 else "medium" if unique_dates / max(days_span, 1) > 0.2 else "low"
        
        return {
            "peak_hours": peak_hours,
            "session_frequency": session_frequency,
            "total_sessions": unique_dates,
            "days_active": days_span
        }
    
    def _find_similar_users(self, user_id: int, db: Session, limit: int = 10) -> List[Tuple[int, float]]:
        """Find users with similar learning patterns"""
        try:
            # Get target user's skill progress
            target_skills = db.query(SkillProgress).filter(
                SkillProgress.user_id == user_id
            ).all()
            
            if not target_skills:
                return []
            
            target_vector = self._create_user_vector(target_skills)
            
            # Get other users' skill progress
            all_users = db.query(User.id).filter(User.id != user_id).all()
            similarities = []
            
            for (other_user_id,) in all_users:
                other_skills = db.query(SkillProgress).filter(
                    SkillProgress.user_id == other_user_id
                ).all()
                
                if other_skills:
                    other_vector = self._create_user_vector(other_skills)
                    similarity = self._calculate_cosine_similarity(target_vector, other_vector)
                    
                    if similarity > self.similarity_threshold:
                        similarities.append((other_user_id, similarity))
            
            # Sort by similarity and return top matches
            similarities.sort(key=lambda x: x[1], reverse=True)
            return similarities[:limit]
            
        except Exception as e:
            logger.error(f"Error finding similar users: {str(e)}")
            return []
    
    def _create_user_vector(self, skill_progress: List[SkillProgress]) -> np.ndarray:
        """Create a vector representation of user's skill progress"""
        # This is a simplified version - could be enhanced with more sophisticated features
        skill_ids = [sp.skill_id for sp in skill_progress]
        progress_values = [sp.progress_percentage for sp in skill_progress]
        
        # Create a sparse vector (in practice, you'd use a more sophisticated approach)
        max_skill_id = max(skill_ids) if skill_ids else 1
        vector = np.zeros(max_skill_id + 1)
        
        for skill_id, progress in zip(skill_ids, progress_values):
            vector[skill_id] = progress / 100.0
        
        return vector
    
    def _calculate_cosine_similarity(self, vec1: np.ndarray, vec2: np.ndarray) -> float:
        """Calculate cosine similarity between two vectors"""
        # Ensure vectors are same length
        max_len = max(len(vec1), len(vec2))
        if len(vec1) < max_len:
            vec1 = np.pad(vec1, (0, max_len - len(vec1)))
        if len(vec2) < max_len:
            vec2 = np.pad(vec2, (0, max_len - len(vec2)))
        
        dot_product = np.dot(vec1, vec2)
        norm1 = np.linalg.norm(vec1)
        norm2 = np.linalg.norm(vec2)
        
        if norm1 == 0 or norm2 == 0:
            return 0.0
        
        return dot_product / (norm1 * norm2)
    
    def _get_popular_recommendations(self, db: Session, limit: int) -> List[Dict[str, Any]]:
        """Get popular skills as fallback recommendations"""
        # Get most popular skills (most users enrolled)
        popular_skills = db.query(
            Skill.id, Skill.name, Skill.description,
            func.count(SkillProgress.user_id).label('user_count')
        ).join(SkillProgress).group_by(Skill.id).order_by(
            desc('user_count')
        ).limit(limit).all()
        
        recommendations = []
        for skill_id, name, description, user_count in popular_skills:
            recommendations.append({
                "type": "skill",
                "item_id": skill_id,
                "title": name,
                "description": description,
                "score": user_count,
                "reason": f"Popular choice among learners ({user_count} users)"
            })
        
        return recommendations
    
    def _default_behavior_analysis(self) -> Dict[str, Any]:
        """Return default behavior analysis for new users"""
        return {
            "learning_style": "balanced",
            "preferred_difficulty": "beginner",
            "engagement_patterns": {"peak_hours": [19, 20, 21], "session_frequency": "medium"},
            "completion_rate": 0.0,
            "average_session_time": 30,
            "struggling_topics": [],
            "strengths": [],
            "learning_pace": "medium",
            "recommended_adjustments": ["Start with beginner-level content", "Maintain regular learning schedule"]
        }
    
    # Additional helper methods would be implemented here...
    def _calculate_completion_rate(self, skill_progress: List[SkillProgress]) -> float:
        """Calculate user's overall completion rate"""
        if not skill_progress:
            return 0.0
        
        total_progress = sum(sp.progress_percentage for sp in skill_progress)
        return total_progress / (len(skill_progress) * 100)
    
    def _identify_struggling_topics(self, quiz_attempts: List[QuizAttempt], 
                                  skill_progress: List[SkillProgress]) -> List[str]:
        """Identify topics where user is struggling"""
        struggling = []
        
        # Analyze quiz performance
        for attempt in quiz_attempts:
            if attempt.score / attempt.total_questions < 0.6:
                skill = next((sp for sp in skill_progress if sp.skill_id == attempt.skill_id), None)
                if skill:
                    struggling.append(skill.skill.name if hasattr(skill, 'skill') else f"Skill {attempt.skill_id}")
        
        return list(set(struggling))
    
    def _estimate_completion_time(self, skill: Skill, learning_pace: str) -> str:
        """Estimate completion time based on skill and user's pace"""
        base_hours = len(skill.subskills) * 8 if skill.subskills else 40  # 8 hours per subskill
        
        pace_multipliers = {"slow": 1.5, "medium": 1.0, "fast": 0.7}
        multiplier = pace_multipliers.get(learning_pace, 1.0)
        
        total_hours = int(base_hours * multiplier)
        weeks = max(1, total_hours // 10)  # Assuming 10 hours per week
        
        return f"{weeks} weeks ({total_hours} hours)"

# Global instance
adaptive_engine = AdaptiveLearningEngine()
