from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Dict, Any
from datetime import datetime, timedelta
from pydantic import BaseModel

from database.database import get_db
from models.models import User, Skill, SkillProgress, XPTransaction, SubskillProgress, UserBehavior
from schemas.schemas import ProgressCreate, ProgressUpdate, ProgressResponse
from utils.auth import get_current_active_user
from utils.adaptive_learning import adaptive_engine

# Enhanced request models
class SubskillProgressRequest(BaseModel):
    skill_id: int
    subskill_name: str
    completed: bool = True
    time_spent_minutes: int = 0
    difficulty_rating: float = None  # 1-5 scale

class StreakUpdateRequest(BaseModel):
    action_type: str  # daily_goal, subskill_complete, quiz_complete
    metadata: Dict[str, Any] = {}

router = APIRouter(
    prefix="/progress",
    tags=["Progress"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=ProgressResponse)
async def create_progress(
    progress: ProgressCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Create a new progress entry for a skill"""
    # Check if skill exists
    skill = db.query(Skill).filter(Skill.id == progress.skill_id).first()
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    
    # Check if progress already exists
    existing_progress = db.query(SkillProgress).filter(
        SkillProgress.user_id == current_user.id,
        SkillProgress.skill_id == progress.skill_id
    ).first()
    
    if existing_progress:
        raise HTTPException(
            status_code=400, 
            detail="Progress for this skill already exists"
        )
    
    # Create progress
    db_progress = SkillProgress(
        user_id=current_user.id,
        skill_id=progress.skill_id,
        progress_percentage=progress.progress_percentage,
        completed=progress.completed
    )
    db.add(db_progress)
    db.commit()
    db.refresh(db_progress)
    
    # Award initial XP for starting a new skill
    xp_transaction = XPTransaction(
        user_id=current_user.id,
        amount=50,  # 50 XP for starting a new skill
        description=f"Started learning: {skill.name}"
    )
    db.add(xp_transaction)
    db.commit()
    
    return db_progress

@router.get("/", response_model=List[ProgressResponse])
async def read_progress(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get all progress entries for the current user"""
    progress = db.query(SkillProgress).filter(
        SkillProgress.user_id == current_user.id
    ).all()
    return progress

@router.get("/skill/{skill_id}")
async def get_skill_progress_enhanced(
    skill_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get enhanced progress for a specific skill including subskill tracking"""
    try:
        # Get main skill progress
        skill_progress = db.query(SkillProgress).filter(
            SkillProgress.user_id == current_user.id,
            SkillProgress.skill_id == skill_id
        ).first()
        
        # Get subskill progress
        subskill_progress = db.query(SubskillProgress).filter(
            SubskillProgress.user_id == current_user.id,
            SubskillProgress.skill_id == skill_id
        ).all()
        
        # Get skill details
        skill = db.query(Skill).filter(Skill.id == skill_id).first()
        if not skill:
            raise HTTPException(status_code=404, detail="Skill not found")
        
        # Calculate detailed progress
        completed_subskills = [sp.subskill_name for sp in subskill_progress if sp.completed]
        total_subskills = len(skill.subskills) if skill.subskills else 0
        
        progress_percentage = (len(completed_subskills) / total_subskills * 100) if total_subskills > 0 else 0
        
        # Update main progress if it exists
        if skill_progress:
            skill_progress.progress_percentage = progress_percentage
            skill_progress.completed_subskills = completed_subskills
            skill_progress.completed = progress_percentage == 100
            db.commit()
        
        return {
            "skill_id": skill_id,
            "skill_name": skill.name,
            "progress_percentage": progress_percentage,
            "completed": progress_percentage == 100,
            "completed_subskills": completed_subskills,
            "total_subskills": total_subskills,
            "has_started": skill_progress is not None,  # Add this field to indicate if skill was started
            "subskill_details": [
                {
                    "name": sp.subskill_name,
                    "completed": sp.completed,
                    "time_spent_minutes": sp.time_spent_minutes,
                    "completed_at": sp.completed_at.isoformat() if sp.completed_at else None,
                    "difficulty_rating": sp.difficulty_rating
                }
                for sp in subskill_progress
            ],
            "total_time_spent": sum(sp.time_spent_minutes for sp in subskill_progress),
            "average_difficulty_rating": sum(sp.difficulty_rating for sp in subskill_progress if sp.difficulty_rating) / len([sp for sp in subskill_progress if sp.difficulty_rating]) if any(sp.difficulty_rating for sp in subskill_progress) else None
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get skill progress: {str(e)}"
        )

@router.post("/subskill/complete")
async def complete_subskill(
    request: SubskillProgressRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Mark a subskill as completed and track detailed progress"""
    try:
        # Get or create subskill progress
        subskill_progress = db.query(SubskillProgress).filter(
            SubskillProgress.user_id == current_user.id,
            SubskillProgress.skill_id == request.skill_id,
            SubskillProgress.subskill_name == request.subskill_name
        ).first()
        
        if not subskill_progress:
            subskill_progress = SubskillProgress(
                user_id=current_user.id,
                skill_id=request.skill_id,
                subskill_name=request.subskill_name
            )
            db.add(subskill_progress)
        
        # Update progress
        subskill_progress.completed = request.completed
        # Ensure time_spent_minutes is not None
        if subskill_progress.time_spent_minutes is None:
            subskill_progress.time_spent_minutes = 0
        subskill_progress.time_spent_minutes += request.time_spent_minutes
        if request.completed:
            subskill_progress.completed_at = datetime.utcnow()
        if request.difficulty_rating:
            subskill_progress.difficulty_rating = request.difficulty_rating
        
        db.commit()
        
        # Track user behavior
        adaptive_engine.track_user_interaction(
            user_id=current_user.id,
            action_type="complete_subskill" if request.completed else "uncomplete_subskill",
            skill_id=request.skill_id,
            subskill_name=request.subskill_name,
            metadata={
                "time_spent_minutes": request.time_spent_minutes,
                "difficulty_rating": request.difficulty_rating
            },
            db=db
        )
        
        # Award XP for completion
        xp_earned = 0
        if request.completed:
            base_xp = 10  # Base XP for completing a subskill
            
            # Bonus XP based on difficulty rating
            if request.difficulty_rating:
                difficulty_bonus = int(request.difficulty_rating * 2)  # 2-10 bonus XP
                base_xp += difficulty_bonus
            
            xp_earned = base_xp
            
            # Create XP transaction
            xp_transaction = XPTransaction(
                user_id=current_user.id,
                amount=xp_earned,
                transaction_type="complete_subskill",
                description=f"Completed subskill: {request.subskill_name}",
                skill_id=request.skill_id
            )
            db.add(xp_transaction)
            
            # Update user's total XP
            user = db.query(User).filter(User.id == current_user.id).first()
            if user:
                # Ensure total_xp is not None
                if user.total_xp is None:
                    user.total_xp = 0
                user.total_xp = int(user.total_xp) + xp_earned
            
            db.commit()
        
        # Update streak
        streak_data = _update_user_streak(current_user.id, db)
        
        return {
            "subskill_name": request.subskill_name,
            "completed": request.completed,
            "xp_earned": xp_earned,
            "current_streak": streak_data["current_streak"],
            "total_xp": streak_data["total_xp"],
            "completed_today": streak_data["completed_today"]
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to update subskill progress: {str(e)}"
        )

@router.post("/subskill/uncomplete")
async def uncomplete_subskill(
    request: SubskillProgressRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Mark a subskill as uncompleted"""
    try:
        # Find and update subskill progress
        subskill_progress = db.query(SubskillProgress).filter(
            SubskillProgress.user_id == current_user.id,
            SubskillProgress.skill_id == request.skill_id,
            SubskillProgress.subskill_name == request.subskill_name
        ).first()
        
        if subskill_progress:
            subskill_progress.completed = False
            subskill_progress.completed_at = None
            db.commit()
        
        # Track user behavior
        adaptive_engine.track_user_interaction(
            user_id=current_user.id,
            action_type="uncomplete_subskill",
            skill_id=request.skill_id,
            subskill_name=request.subskill_name,
            db=db
        )
        
        return {"message": "Subskill marked as incomplete"}
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to uncomplete subskill: {str(e)}"
        )

@router.get("/analytics")
async def get_progress_analytics(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get comprehensive progress analytics for the user"""
    try:
        # Get user behavior analysis
        behavior_analysis = adaptive_engine.analyze_user_behavior(current_user.id, db)
        
        # Get all user's progress
        skill_progress = db.query(SkillProgress).filter(
            SkillProgress.user_id == current_user.id
        ).all()
        
        # Get recent activity
        recent_activity = db.query(UserBehavior).filter(
            UserBehavior.user_id == current_user.id
        ).order_by(UserBehavior.timestamp.desc()).limit(20).all()
        
        # Calculate statistics
        total_skills = len(skill_progress)
        completed_skills = len([sp for sp in skill_progress if sp.completed])
        avg_progress = sum(sp.progress_percentage for sp in skill_progress) / total_skills if total_skills > 0 else 0
        
        # Get XP history
        xp_transactions = db.query(XPTransaction).filter(
            XPTransaction.user_id == current_user.id
        ).order_by(XPTransaction.created_at.desc()).limit(10).all()
        
        return {
            "behavior_analysis": behavior_analysis,
            "progress_summary": {
                "total_skills": total_skills,
                "completed_skills": completed_skills,
                "completion_rate": completed_skills / total_skills if total_skills > 0 else 0,
                "average_progress": avg_progress
            },
            "recent_activity": [
                {
                    "action_type": activity.action_type,
                    "skill_id": activity.skill_id,
                    "subskill_name": activity.subskill_name,
                    "timestamp": activity.timestamp.isoformat(),
                    "metadata": activity.metadata
                }
                for activity in recent_activity
            ],
            "xp_history": [
                {
                    "amount": xp.amount,
                    "transaction_type": xp.transaction_type,
                    "description": xp.description,
                    "created_at": xp.created_at.isoformat()
                }
                for xp in xp_transactions
            ],
            "streak_info": {
                "current_streak": current_user.current_streak,
                "longest_streak": current_user.longest_streak,
                "total_xp": current_user.total_xp
            }
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get progress analytics: {str(e)}"
        )

def _update_user_streak(user_id: int, db: Session) -> Dict[str, Any]:
    """Update user's learning streak"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return {"current_streak": 0, "total_xp": 0, "completed_today": False}
    
    today = datetime.now().date()
    last_activity_date = user.last_activity.date() if user.last_activity else None
    
    # Check if user has activity today
    today_activity = db.query(UserBehavior).filter(
        UserBehavior.user_id == user_id,
        UserBehavior.timestamp >= datetime.combine(today, datetime.min.time()),
        UserBehavior.action_type.in_(["complete_subskill", "complete_quiz"])
    ).first()
    
    completed_today = bool(today_activity)
    
    # Update streak
    if last_activity_date == today:
        # Already active today, maintain streak
        pass
    elif last_activity_date == today - timedelta(days=1):
        # Active yesterday, increment streak
        if user.current_streak is None:
            user.current_streak = 0
        user.current_streak += 1
        if user.longest_streak is None:
            user.longest_streak = 0
        if user.current_streak > user.longest_streak:
            user.longest_streak = user.current_streak
    elif last_activity_date and last_activity_date < today - timedelta(days=1):
        # Streak broken, reset
        user.current_streak = 1
    else:
        # First activity or no previous activity
        user.current_streak = 1
    
    user.last_activity = datetime.utcnow()
    db.commit()
    
    return {
        "current_streak": user.current_streak or 0,
        "total_xp": user.total_xp or 0,
        "completed_today": completed_today
    }

@router.patch("/{skill_id}", response_model=ProgressResponse)
async def update_skill_progress(
    skill_id: int,
    progress_update: ProgressUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Update progress for a specific skill"""
    # Get existing progress
    db_progress = db.query(SkillProgress).filter(
        SkillProgress.user_id == current_user.id,
        SkillProgress.skill_id == skill_id
    ).first()
    
    if not db_progress:
        raise HTTPException(status_code=404, detail="Progress not found")
      # Calculate XP gain
    old_percentage = db_progress.progress_percentage
    new_percentage = progress_update.progress_percentage if progress_update.progress_percentage is not None else old_percentage
    
    # Check if skill is being completed
    was_completed = db_progress.completed
    will_be_completed = progress_update.completed if progress_update.completed is not None else was_completed
    completion_bonus = 0
    
    if will_be_completed and not was_completed:
        completion_bonus = 200  # 200 XP bonus for completing a skill
    
    # Update progress fields
    update_data = progress_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_progress, key, value)
    
    db.commit()
    db.refresh(db_progress)
      # Award XP for progress
    if new_percentage > old_percentage or completion_bonus > 0:
        xp_gained = int((new_percentage - old_percentage) * 10) + completion_bonus  # 10 XP per percentage point + completion bonus
        
        # Get skill name for better description
        skill = db.query(Skill).filter(Skill.id == skill_id).first()
        skill_name = skill.name if skill else f"Skill #{skill_id}"
        
        # Create XP transaction
        xp_transaction = XPTransaction(
            user_id=current_user.id,
            amount=xp_gained,
            description=f"Progress on {skill_name}" + (f" (Completed! +{completion_bonus} XP)" if completion_bonus > 0 else "")
        )
        db.add(xp_transaction)
        db.commit()
        
        # If a skill was completed, check if it's part of a learning path (has a parent)
        if will_be_completed and not was_completed and skill and skill.parent_id:
            # Check if all sibling skills are completed
            sibling_skills = db.query(Skill).filter(Skill.parent_id == skill.parent_id).all()
            sibling_skill_ids = [s.id for s in sibling_skills]
            
            # Get progress for all sibling skills
            sibling_progress = db.query(SkillProgress).filter(
                SkillProgress.user_id == current_user.id,
                SkillProgress.skill_id.in_(sibling_skill_ids)
            ).all()
            
            # Check if all siblings have progress and are completed
            all_completed = (
                len(sibling_progress) == len(sibling_skills) and 
                all(p.completed for p in sibling_progress)
            )
            
            # If all siblings are completed, update the parent skill's progress
            if all_completed:
                parent_progress = db.query(SkillProgress).filter(
                    SkillProgress.user_id == current_user.id,
                    SkillProgress.skill_id == skill.parent_id
                ).first()
                
                if parent_progress:
                    # Update parent progress to 100% and mark as completed
                    parent_progress.progress_percentage = 100
                    parent_progress.completed = True
                    db.commit()
                    
                    # Award XP for completing the learning path
                    path_xp_transaction = XPTransaction(
                        user_id=current_user.id,
                        amount=500,  # 500 XP for completing an entire learning path
                        description=f"Completed learning path: {skill.parent.name if skill.parent else 'Unknown'}"
                    )
                    db.add(path_xp_transaction)
                    db.commit()
    
    return db_progress
