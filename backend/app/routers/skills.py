from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Dict, Any
from pydantic import BaseModel

from database.database import get_db
from models.models import Skill, User, SkillProgress
from schemas.schemas import SkillCreate, SkillResponse, SkillTree, SkillNameRequest
from utils.auth import get_current_active_user
from utils.llm_integration import llm_integration
from utils.adaptive_learning import adaptive_engine
from utils.quiz_generator import quiz_manager

# Import ML functions
import sys
import os
# Append the project root to access the ml directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
from ml.skill_decomposition import decompose_skill, generate_learning_path

# Enhanced request models
class SkillDecomposeRequest(BaseModel):
    skill_name: str
    user_level: str = "beginner"  # beginner, intermediate, advanced
    use_ai: bool = True

class PersonalizedPathRequest(BaseModel):
    skill_name: str
    time_available_hours: int = 10  # hours per week
    preferred_difficulty: str = "adaptive"
    learning_style: str = "balanced"  # visual, reading, hands-on, balanced

router = APIRouter(
    prefix="/skills",
    tags=["Skills"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=SkillResponse)
async def create_skill(
    skill: SkillCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Create a new skill in the database"""
    db_skill = Skill(
        name=skill.name,
        description=skill.description,
        parent_id=skill.parent_id
    )
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill

@router.get("/", response_model=List[SkillResponse])
async def read_skills(
    skip: int = 0, 
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Get all skills"""
    skills = db.query(Skill).offset(skip).limit(limit).all()
    return skills

@router.get("/{skill_id}", response_model=SkillResponse)
async def read_skill(
    skill_id: int,
    db: Session = Depends(get_db)
):
    """Get a specific skill by ID"""
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if skill is None:
        raise HTTPException(status_code=404, detail="Skill not found")
    return skill

@router.post("/decompose", response_model=dict)
async def decompose_skill_endpoint(
    request: SkillDecomposeRequest,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Decompose a skill into subskills using AI or ML-based methods
    """
    try:
        if request.use_ai:
            # Use AI-powered decomposition
            skill_data = llm_integration.decompose_skill_with_llm(
                skill_name=request.skill_name,
                user_level=request.user_level
            )
            
            # Create or update skill in database
            if "error" not in skill_data:
                existing_skill = db.query(Skill).filter(Skill.name == request.skill_name).first()
                
                if not existing_skill:
                    new_skill = Skill(
                        name=request.skill_name,
                        description=skill_data.get('description', f'AI-generated learning path for {request.skill_name}'),
                        difficulty_level=request.user_level,
                        estimated_duration=skill_data.get('estimated_duration'),
                        subskills=[subskill['name'] for subskill in skill_data.get('subskills', [])],
                        created_by_ai=True
                    )
                    db.add(new_skill)
                    db.commit()
                    db.refresh(new_skill)
                    
                    skill_data['skill_id'] = new_skill.id
                else:
                    skill_data['skill_id'] = existing_skill.id
            
            return skill_data
        else:
            # Use traditional ML-based decomposition
            skill_tree = decompose_skill(request.skill_name)
            
            # Create or get skill in database
            existing_skill = db.query(Skill).filter(Skill.name == request.skill_name).first()
            
            if not existing_skill:
                # Extract subskills from the tree structure
                subskills = []
                if 'children' in skill_tree:
                    subskills = [child['name'] for child in skill_tree['children']]
                
                new_skill = Skill(
                    name=request.skill_name,
                    description=f'ML-generated learning path for {request.skill_name}',
                    difficulty_level=request.user_level,
                    subskills=subskills,
                    created_by_ai=False
                )
                db.add(new_skill)
                db.commit()
                db.refresh(new_skill)
                
                skill_tree['skill_id'] = new_skill.id
            else:
                skill_tree['skill_id'] = existing_skill.id
            
            return skill_tree
            
    except Exception as e:
        # Fallback to traditional method
        skill_tree = decompose_skill(request.skill_name)
        return skill_tree

@router.post("/learning-path", response_model=dict)
async def generate_learning_path_endpoint(
    request: PersonalizedPathRequest,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Generate a personalized learning path for a given skill
    """
    try:
        # Check if skill exists in database
        skill = db.query(Skill).filter(Skill.name == request.skill_name).first()
        
        if skill:
            # Generate personalized path using adaptive engine
            learning_path = adaptive_engine.generate_personalized_learning_path(
                user_id=current_user.id,
                skill_id=skill.id,
                db=db
            )
            return learning_path
        else:
            # Create new skill using AI decomposition
            skill_data = llm_integration.decompose_skill_with_llm(
                skill_name=request.skill_name,
                user_level=request.preferred_difficulty if request.preferred_difficulty != "adaptive" else "beginner"
            )
            
            if "error" not in skill_data:
                # Create skill in database
                new_skill = Skill(
                    name=request.skill_name,
                    description=skill_data.get('description'),
                    difficulty_level=skill_data.get('difficulty', 'beginner'),
                    estimated_duration=skill_data.get('estimated_duration'),
                    subskills=[subskill['name'] for subskill in skill_data.get('subskills', [])],
                    created_by_ai=True
                )
                db.add(new_skill)
                db.commit()
                db.refresh(new_skill)
                
                # Generate personalized path
                learning_path = adaptive_engine.generate_personalized_learning_path(
                    user_id=current_user.id,
                    skill_id=new_skill.id,
                    db=db
                )
                return learning_path
            else:
                # Fallback to traditional method
                path = generate_learning_path(request.skill_name)
                return {"skill_name": request.skill_name, "path": path}
                
    except Exception as e:
        # Fallback to traditional method
        path = generate_learning_path(request.skill_name)
        return {"skill_name": request.skill_name, "path": path}

@router.get("/{skill_id}/personalized-path")
async def get_personalized_path(
    skill_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Get a personalized learning path for an existing skill
    """
    try:
        skill = db.query(Skill).filter(Skill.id == skill_id).first()
        if not skill:
            raise HTTPException(status_code=404, detail="Skill not found")
        
        # Generate personalized path
        learning_path = adaptive_engine.generate_personalized_learning_path(
            user_id=current_user.id,
            skill_id=skill_id,
            db=db
        )
        
        return learning_path
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate personalized path: {str(e)}"
        )

@router.get("/{skill_id}/analytics")
async def get_skill_analytics(
    skill_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Get detailed analytics for a skill including difficulty adjustment and user behavior
    """
    try:
        skill = db.query(Skill).filter(Skill.id == skill_id).first()
        if not skill:
            raise HTTPException(status_code=404, detail="Skill not found")
        
        # Get user behavior analysis
        behavior_analysis = adaptive_engine.analyze_user_behavior(current_user.id, db)
        
        # Get difficulty adjustment recommendations
        difficulty_analysis = adaptive_engine.adjust_difficulty_dynamically(
            user_id=current_user.id,
            skill_id=skill_id,
            db=db
        )
        
        # Get user's progress on this skill
        progress = db.query(SkillProgress).filter(
            SkillProgress.user_id == current_user.id,
            SkillProgress.skill_id == skill_id
        ).first()
        
        return {
            "skill_id": skill_id,
            "skill_name": skill.name,
            "user_progress": {
                "progress_percentage": progress.progress_percentage if progress else 0.0,
                "completed": progress.completed if progress else False,
                "completed_subskills": progress.completed_subskills if progress else [],
                "average_quiz_score": progress.average_quiz_score if progress else 0.0
            },
            "behavior_analysis": behavior_analysis,
            "difficulty_analysis": difficulty_analysis,
            "recommendations": adaptive_engine.get_collaborative_recommendations(
                user_id=current_user.id,
                db=db,
                limit=3
            )
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get skill analytics: {str(e)}"
        )

@router.get("/{skill_id}/quiz")
async def get_skill_quiz(
    skill_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Get adaptive quiz questions for a specific skill
    """
    try:
        # Use the enhanced quiz manager for adaptive quiz generation
        quiz_data = quiz_manager.generate_skill_quiz(
            skill_id=skill_id,
            user_id=current_user.id,
            num_questions=5,
            db=db
        )
        
        # Track user interaction
        adaptive_engine.track_user_interaction(
            user_id=current_user.id,
            action_type="request_quiz",
            skill_id=skill_id,
            db=db
        )
        
        return quiz_data
        
    except Exception as e:
        # Fallback to basic quiz if enhanced generation fails
        skill = db.query(Skill).filter(Skill.id == skill_id).first()
        if skill is None:
            raise HTTPException(status_code=404, detail="Skill not found")
        
        fallback_questions = [
            {
                "question": f"What is the primary purpose of {skill.name}?",
                "options": [
                    "To solve computational problems",
                    "To create user interfaces", 
                    "To manage databases",
                    "To handle network requests"
                ],
                "correct_answer": "To solve computational problems",
                "explanation": f"This question tests basic understanding of {skill.name}.",
                "difficulty": "easy"
            },
            {
                "question": f"Which is considered a best practice when learning {skill.name}?",
                "options": [
                    "Practice regularly with hands-on projects",
                    "Only read theoretical materials",
                    "Skip fundamentals and jump to advanced topics",
                    "Avoid asking questions"
                ],
                "correct_answer": "Practice regularly with hands-on projects",
                "explanation": "Regular practice with real projects is essential for skill development.",
                "difficulty": "medium"
            }
        ]
        
        return {
            "skill_id": skill_id,
            "skill_name": skill.name,
            "questions": fallback_questions,
            "total_questions": len(fallback_questions),
            "estimated_time_minutes": 4,
            "difficulty_level": "beginner"
        }

@router.post("/ai-generate")
async def generate_skill_with_ai(
    request: SkillDecomposeRequest,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Generate a complete skill with AI including subskills, resources, and quiz questions
    """
    try:
        # Generate skill decomposition with AI
        skill_data = llm_integration.decompose_skill_with_llm(
            skill_name=request.skill_name,
            user_level=request.user_level
        )
        
        if "error" in skill_data:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to generate skill with AI"
            )
        
        # Create skill in database
        new_skill = Skill(
            name=request.skill_name,
            description=skill_data.get('description', f'AI-generated learning path for {request.skill_name}'),
            difficulty_level=request.user_level,
            estimated_duration=skill_data.get('estimated_duration'),
            subskills=[subskill['name'] for subskill in skill_data.get('subskills', [])],
            created_by_ai=True
        )
        
        db.add(new_skill)
        db.commit()
        db.refresh(new_skill)
        
        # Generate quiz questions for each subskill
        for subskill_data in skill_data.get('subskills', []):
            quiz_questions = llm_integration.generate_quiz_questions(
                subskill_name=subskill_data['name'],
                num_questions=3
            )
            
            # Save quiz questions to database
            from models.models import QuizQuestion
            for question_data in quiz_questions:
                quiz_question = QuizQuestion(
                    skill_id=new_skill.id,
                    subskill_name=subskill_data['name'],
                    question=question_data.get('question'),
                    options=question_data.get('options', []),
                    correct_answer=question_data.get('correct_answer'),
                    explanation=question_data.get('explanation'),
                    difficulty=question_data.get('difficulty', 'medium'),
                    created_by_ai=True
                )
                db.add(quiz_question)
        
        db.commit()
        
        return {
            "skill_id": new_skill.id,
            "skill_data": skill_data,
            "message": f"Successfully generated {request.skill_name} with AI including subskills and quiz questions"
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate skill with AI: {str(e)}"
        )
