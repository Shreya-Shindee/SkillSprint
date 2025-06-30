from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Dict
import logging

from database.database import get_db
from models.models import Resource, User, Skill
from schemas.schemas import ResourceCreate, ResourceResponse, SkillNameRequest, ResourceRecommendation
from utils.auth import get_current_active_user

# Import ML functions for resource recommendation
import sys
import os
# Append the project root to access the ml directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
from ml.skill_decomposition import get_resources_for_skill

router = APIRouter(
    prefix="/resources",
    tags=["Resources"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=ResourceResponse)
async def create_resource(
    resource: ResourceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Create a new learning resource"""
    # Check if skill exists
    skill = db.query(Skill).filter(Skill.id == resource.skill_id).first()
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    
    # Create resource
    db_resource = Resource(
        title=resource.title,
        url=resource.url,
        description=resource.description,
        resource_type=resource.resource_type,
        skill_id=resource.skill_id
    )
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

@router.get("/", response_model=List[ResourceResponse])
async def read_resources(
    skip: int = 0, 
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Get all resources"""
    resources = db.query(Resource).offset(skip).limit(limit).all()
    return resources

@router.get("/search")
async def search_resources(
    skill: str,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Search for resources by skill name with fast fallback"""
    try:
        logger = logging.getLogger(__name__)
        logger.info(f"Searching resources for skill: {skill}")
        
        # Try fast fallback first for instant response
        try:
            from utils.fast_fallback import get_fast_fallback_resources
            fast_resources = get_fast_fallback_resources(skill)
            if fast_resources:
                logger.info(f"Fast fallback found {len(fast_resources)} resources for {skill}")
                resources = fast_resources[:limit]
            else:
                # No fast fallback, try basic search
                from utils.resource_search import get_resources_for_skill
                resources = get_resources_for_skill(skill, max_per_type=limit//3 + 1)
                logger.info(f"Basic search found {len(resources)} resources for {skill}")
        except Exception as e:
            logger.warning(f"Search failed, using fallback: {e}")
            # Fallback to basic resource search
            from utils.resource_search import get_resources_for_skill
            resources = get_resources_for_skill(skill, max_per_type=limit//3 + 1)
        
        # Sort by quality score and limit results
        resources.sort(key=lambda x: x.get('quality_score', 0), reverse=True)
        resources = resources[:limit]
        
        logger.info(f"Returning {len(resources)} resources for {skill}")
        
        return {
            "resources": resources,
            "total": len(resources),
            "skill": skill
        }
        
    except Exception as e:
        logger.error(f"Error searching resources for {skill}: {str(e)}")
        # Return fallback resources
        fallback_resources = [
            {
                "title": f"Learn {skill} - Free Tutorial",
                "url": "https://www.freecodecamp.org/",
                "description": f"Comprehensive tutorial for learning {skill}",
                "resource_type": "article",
                "quality_score": 70
            },
            {
                "title": f"{skill} Documentation",
                "url": f"https://docs.python.org/3/" if "python" in skill.lower() else "https://developer.mozilla.org/",
                "description": f"Official documentation for {skill}",
                "resource_type": "documentation", 
                "quality_score": 90
            }
        ]
        
        return {
            "resources": fallback_resources,
            "total": len(fallback_resources),
            "skill": skill
        }

@router.get("/learning-path/{skill_name}")
async def get_learning_path_with_resources(
    skill_name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get a complete learning path with resources and quizzes for a skill"""
    try:
        logger = logging.getLogger(__name__)
        logger.info(f"Generating learning path for: {skill_name}")
        
        # Import the enhanced resource search
        from utils.enhanced_resource_search import get_enhanced_resources_with_path
        
        # Get enhanced resources and learning path
        learning_data = await get_enhanced_resources_with_path(skill_name)
        
        return {
            "skill": skill_name,
            "learning_path": learning_data["learning_path"],
            "resources": learning_data["resources"],
            "total_resources": learning_data["total_resources"],
            "estimated_duration": learning_data["estimated_duration"]
        }
        
    except Exception as e:
        logger.error(f"Error generating learning path for {skill_name}: {str(e)}")
        
        # Return a basic learning path structure
        from utils.resource_search import get_resources_for_skill
        basic_resources = get_resources_for_skill(skill_name, max_per_type=3)
        
        return {
            "skill": skill_name,
            "learning_path": {
                "phases": [
                    {
                        "name": "Foundation",
                        "description": "Learn the basics and core concepts",
                        "duration": "1-2 weeks",
                        "resources": basic_resources[:3],
                        "quiz": []
                    },
                    {
                        "name": "Practice",
                        "description": "Apply your knowledge with hands-on practice",
                        "duration": "2-3 weeks", 
                        "resources": basic_resources[3:6],
                        "quiz": []
                    }
                ],
                "total_duration": "3-5 weeks"
            },
            "resources": basic_resources,
            "total_resources": len(basic_resources),
            "estimated_duration": "3-5 weeks"
        }

@router.get("/skill/{skill_id}", response_model=List[ResourceResponse])
async def read_resources_by_skill(
    skill_id: int,
    db: Session = Depends(get_db)
):
    """Get all resources for a specific skill"""
    # Check if skill exists
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    
    resources = db.query(Resource).filter(Resource.skill_id == skill_id).all()
    return resources

@router.get("/{resource_id}", response_model=ResourceResponse)
async def read_resource(
    resource_id: int,
    db: Session = Depends(get_db)
):
    """Get a specific resource by ID"""    
    resource = db.query(Resource).filter(Resource.id == resource_id).first()
    if resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource

@router.post("/by-skill-name", response_model=Dict[str, List[dict]])
async def get_resources_by_skill_name(
    request: SkillNameRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get resources for a skill by name and generate recommendations if none exist"""
    skill_name = request.skill_name
    
    # Try to find the skill by name
    skill = db.query(Skill).filter(Skill.name == skill_name).first()
    
    resources_by_skill = {}
    
    if skill:
        # If skill exists, get its resources
        resources = db.query(Resource).filter(Resource.skill_id == skill.id).all()
        # Convert SQLAlchemy models to dictionaries
        resources_by_skill[skill_name] = [
            {
                "id": r.id,
                "title": r.title,
                "url": r.url,
                "description": r.description,
                "resource_type": r.resource_type,
                "skill_id": r.skill_id
            } for r in resources
        ]
    else:
        # No resources found, return empty list
        resources_by_skill[skill_name] = []
      # Add default resources if none exist
    if not resources_by_skill[skill_name]:
        default_resources = generate_default_resources(skill_name)
        # default_resources now returns dictionaries directly with quality_score
        resources_by_skill[skill_name] = default_resources
        
    return resources_by_skill

def generate_default_resources(skill_name):
    """
    Generate default resources for a skill using the ML module and dynamic search
    
    Args:
        skill_name (str): The name of the skill
        
    Returns:
        list: List of Resource objects
    """
    # Log that we're generating resources
    logger = logging.getLogger(__name__)
    logger.info(f"Dynamically generating resources for skill: {skill_name}")
    
    # Use the ML function to get recommended resources
    try:
        # Import directly from utils to make sure we're using the most up-to-date version
        from utils.resource_search import get_resources_for_skill as direct_search
        
        # Try to get resources directly first (more reliable than going through ML module)
        dynamic_resources = direct_search(skill_name)
        if dynamic_resources and len(dynamic_resources) > 0:
            logger.info(f"Found {len(dynamic_resources)} dynamic resources directly for {skill_name}")
            recommended_resources = dynamic_resources
        else:
            # Fall back to ML module if direct search fails
            logger.info(f"Direct search returned no results, trying ML module for {skill_name}")
            recommended_resources = get_resources_for_skill(skill_name)
    except Exception as e:
        # If there's an error, fall back to ML module
        logger.warning(f"Error in direct search: {str(e)}, falling back to ML module")
        recommended_resources = get_resources_for_skill(skill_name)
      # Convert to dictionaries with quality scores preserved
    resources = []
    for res in recommended_resources:
        resource_dict = {
            "id": 0,  # Temporary ID
            "title": res["title"],
            "url": res["url"],
            "description": res["description"],
            "resource_type": res["resource_type"],
            "skill_id": None,
            "quality_score": res.get("quality_score", 0)  # Preserve quality score
        }
        resources.append(resource_dict)
    
    logger.info(f"Generated {len(resources)} resources for {skill_name}")
    return resources

@router.post("/search/batch")
async def batch_search_resources(
    skills: List[str],
    limit_per_skill: int = 4,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Batch search for resources for multiple skills at once for better performance"""
    try:
        logger = logging.getLogger(__name__)
        logger.info(f"Batch searching resources for {len(skills)} skills")
        
        results = {}
        
        # Process skills directly (no threading overhead for fast fallback)
        for skill_name in skills:
            try:
                # Try fast fallback first for speed
                from utils.fast_fallback import get_fast_fallback_resources
                logger.info(f"Searching for skill: '{skill_name}'")
                fast_resources = get_fast_fallback_resources(skill_name)
                if fast_resources:
                    resources = fast_resources[:limit_per_skill]
                    logger.info(f"Fast fallback found {len(resources)} resources for '{skill_name}': {resources[0]['title'] if resources else 'none'}")
                    results[skill_name] = resources
                else:
                    # No fast fallback, add generic fallback
                    results[skill_name] = [
                        {
                            "title": f"Learn {skill_name} - Free Tutorial",
                            "url": "https://www.freecodecamp.org/",
                            "description": f"Comprehensive tutorial for {skill_name}",
                            "resource_type": "course",
                            "quality_score": 80
                        }
                    ]
            except Exception as e:
                logger.error(f"Error processing {skill_name}: {e}")
                results[skill_name] = []
        
        logger.info(f"Batch search completed for {len(skills)} skills")
        
        return {
            "results": results,
            "total_skills": len(skills),
            "status": "success"
        }
        
    except Exception as e:
        logger.error(f"Error in batch search: {str(e)}")
        # Return error response with fallback
        fallback_results = {}
        for skill in skills:
            fallback_results[skill] = [
                {
                    "title": f"Learn {skill} - Free Tutorial",
                    "url": "https://www.freecodecamp.org/",
                    "description": f"Comprehensive tutorial for {skill}",
                    "resource_type": "course",
                    "quality_score": 80
                }
            ]
        
        return {
            "results": fallback_results,
            "total_skills": len(skills),
            "status": "fallback",
            "error": str(e)
        }

@router.get("/test-speed")
async def test_speed():
    """Test endpoint speed without authentication"""
    from utils.fast_fallback import get_fast_fallback_resources
    resources = get_fast_fallback_resources("React")
    return {"resources": resources, "count": len(resources)}
