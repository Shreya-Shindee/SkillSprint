import asyncio
from utils.lightweight_search import LightweightResourceSearch
from database.database import SessionLocal
from models.models import Skill, Resource

async def precompute_common_skills():
    """Pre-generate resources for popular skills"""
    common_skills = [
        "Python", "JavaScript", "React", "Node.js", "SQL", 
        "Machine Learning", "Data Science", "HTML", "CSS", "Git"
    ]
    
    db = SessionLocal()
    async with LightweightResourceSearch() as searcher:
        for skill in common_skills:
            print(f"Pre-computing resources for {skill}...")
            resources = await searcher.get_resources_fast(skill)
            
            # Store in database
            for resource_data in resources:
                db_resource = Resource(
                    title=resource_data["title"],
                    url=resource_data["url"],
                    description=resource_data["description"],
                    resource_type=resource_data["resource_type"],
                    quality_score=resource_data["quality_score"]
                )
                db.add(db_resource)
        
        db.commit()
    db.close()

if __name__ == "__main__":
    asyncio.run(precompute_common_skills())