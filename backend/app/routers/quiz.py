"""
Quiz Router - Handles quiz generation, submission, and adaptive assessment
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Dict, Any
from pydantic import BaseModel
from database.database import get_db
from utils.auth import get_current_user
from utils.quiz_generator import quiz_manager
from utils.adaptive_learning import adaptive_engine
from models.models import User, Skill, QuizAttempt
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/quiz", tags=["quiz"])

# Pydantic models for request/response
class QuizRequest(BaseModel):
    skill_id: int
    num_questions: int = 5
    difficulty: str = "adaptive"  # adaptive, easy, medium, hard

class QuizSubmission(BaseModel):
    skill_id: int
    questions: List[Dict[str, Any]]
    user_answers: List[str]
    time_taken_seconds: int

class QuizResponse(BaseModel):
    quiz_id: str
    skill_id: int
    skill_name: str
    questions: List[Dict[str, Any]]
    total_questions: int
    estimated_time_minutes: int
    difficulty_level: str

class QuizResult(BaseModel):
    score: int
    total_questions: int
    score_percentage: float
    time_taken_seconds: int
    xp_earned: int
    performance_level: str
    feedback: List[Dict[str, Any]]
    recommendations: List[str]

@router.post("/generate", response_model=QuizResponse)
async def generate_quiz(
    request: QuizRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Generate an adaptive quiz for a specific skill
    """
    try:
        # Verify skill exists
        skill = db.query(Skill).filter(Skill.id == request.skill_id).first()
        if not skill:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Skill not found"
            )
        
        # Generate quiz using the quiz manager
        quiz_data = quiz_manager.generate_skill_quiz(
            skill_id=request.skill_id,
            user_id=current_user.id,
            num_questions=request.num_questions,
            db=db
        )
        
        # Track user interaction
        adaptive_engine.track_user_interaction(
            user_id=current_user.id,
            action_type="start_quiz",
            skill_id=request.skill_id,
            metadata={"num_questions": request.num_questions},
            db=db
        )
        
        return QuizResponse(
            quiz_id=f"quiz_{current_user.id}_{request.skill_id}_{int(time.time())}",
            **quiz_data
        )
        
    except Exception as e:
        logger.error(f"Error generating quiz: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate quiz"
        )

@router.post("/submit", response_model=QuizResult)
async def submit_quiz(
    submission: QuizSubmission,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Submit quiz answers and get results with adaptive feedback
    """
    try:
        # Validate submission
        if len(submission.user_answers) != len(submission.questions):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Number of answers doesn't match number of questions"
            )
        
        # Process quiz submission
        result = quiz_manager.submit_quiz_attempt(
            user_id=current_user.id,
            skill_id=submission.skill_id,
            questions=submission.questions,
            user_answers=submission.user_answers,
            time_taken=submission.time_taken_seconds,
            db=db
        )
        
        # Track completion interaction
        adaptive_engine.track_user_interaction(
            user_id=current_user.id,
            action_type="complete_quiz",
            skill_id=submission.skill_id,
            metadata={
                "score": result["score"],
                "total_questions": result["total_questions"],
                "time_taken": submission.time_taken_seconds
            },
            db=db
        )
        
        return QuizResult(**result)
        
    except Exception as e:
        logger.error(f"Error submitting quiz: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to submit quiz"
        )

@router.get("/history/{skill_id}")
async def get_quiz_history(
    skill_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get user's quiz history for a specific skill
    """
    try:
        quiz_attempts = db.query(QuizAttempt).filter(
            QuizAttempt.user_id == current_user.id,
            QuizAttempt.skill_id == skill_id
        ).order_by(QuizAttempt.completed_at.desc()).limit(10).all()
        
        history = []
        for attempt in quiz_attempts:
            history.append({
                "id": attempt.id,
                "score": attempt.score,
                "total_questions": attempt.total_questions,
                "score_percentage": (attempt.score / attempt.total_questions) * 100,
                "time_taken_seconds": attempt.time_taken_seconds,
                "completed_at": attempt.completed_at.isoformat()
            })
        
        return {"quiz_history": history}
        
    except Exception as e:
        logger.error(f"Error fetching quiz history: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch quiz history"
        )

@router.get("/analytics/{skill_id}")
async def get_quiz_analytics(
    skill_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get detailed analytics for user's performance on a skill
    """
    try:
        # Get difficulty adjustment analysis
        difficulty_analysis = adaptive_engine.adjust_difficulty_dynamically(
            user_id=current_user.id,
            skill_id=skill_id,
            db=db
        )
        
        # Get recent quiz attempts for trend analysis
        recent_attempts = db.query(QuizAttempt).filter(
            QuizAttempt.user_id == current_user.id,
            QuizAttempt.skill_id == skill_id
        ).order_by(QuizAttempt.completed_at.desc()).limit(10).all()
        
        # Calculate trends
        score_trend = []
        time_trend = []
        
        for attempt in reversed(recent_attempts):
            score_percentage = (attempt.score / attempt.total_questions) * 100
            score_trend.append({
                "date": attempt.completed_at.isoformat(),
                "score_percentage": score_percentage
            })
            time_trend.append({
                "date": attempt.completed_at.isoformat(),
                "time_seconds": attempt.time_taken_seconds
            })
        
        return {
            "difficulty_analysis": difficulty_analysis,
            "score_trend": score_trend,
            "time_trend": time_trend,
            "total_attempts": len(recent_attempts),
            "best_score": max([a.score / a.total_questions for a in recent_attempts]) * 100 if recent_attempts else 0,
            "average_score": sum([a.score / a.total_questions for a in recent_attempts]) / len(recent_attempts) * 100 if recent_attempts else 0
        }
        
    except Exception as e:
        logger.error(f"Error fetching quiz analytics: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch quiz analytics"
        )

@router.get("/recommendations")
async def get_quiz_recommendations(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get personalized quiz recommendations based on user behavior
    """
    try:
        # Get collaborative filtering recommendations
        recommendations = adaptive_engine.get_collaborative_recommendations(
            user_id=current_user.id,
            db=db,
            limit=5
        )
        
        return {"recommendations": recommendations}
        
    except Exception as e:
        logger.error(f"Error fetching quiz recommendations: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch recommendations"
        )

import time