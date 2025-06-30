from sqlalchemy.orm import Session
from database.database import SessionLocal
from models.models import User, Skill, Resource, SkillProgress, XPTransaction
from utils.auth import get_password_hash
from sqlalchemy import text

def seed_data(force=False):
    db = SessionLocal()
    
    try:
        # Check if data already exists
        if db.query(User).count() > 0 and not force:
            print("Data already seeded. Skipping.")
            return
            
        # If force is True, clear existing data first
        if force:
            print("Force flag detected. Clearing existing data...")
            try:
                # Use the reset_db function to safely clear all tables
                from database.reset_db import reset_db
                if not reset_db():
                    print("Failed to reset database. Aborting seed operation.")
                    return
                print("Existing data cleared. Proceeding with seed...")
            except Exception as e:
                print(f"Error clearing database: {e}")
                print("Could not clear existing data. Please run reset_db.py first.")
                return
        
        # Create a test user
        test_user = User(
            email="test@example.com",
            username="testuser",
            hashed_password=get_password_hash("password123")
        )
        db.add(test_user)
        db.commit()
        db.refresh(test_user)
          # Create some skills
        skills = [
            Skill(name="Data Science", description="The field of study that combines domain expertise, programming skills, and knowledge of mathematics and statistics to extract meaningful insights from data."),
            Skill(name="Web Development", description="The work involved in developing a website for the Internet or an intranet."),
            Skill(name="Mobile Development", description="The set of processes and procedures involved in writing software for small, wireless computing devices."),
            Skill(name="Artificial Intelligence", description="The simulation of human intelligence processes by machines, especially computer systems."),
            Skill(name="DevOps", description="A set of practices that combines software development and IT operations to shorten the systems development life cycle."),
            Skill(name="Cloud Computing", description="The delivery of different services through the Internet, including data storage, servers, databases, networking, and software.")
        ]
        
        for skill in skills:
            db.add(skill)
        
        db.commit()
          # Create sub-skills
        parent_skill = db.query(Skill).filter(Skill.name == "Data Science").first()
        
        subskills = [
            Skill(name="Python Basics", description="Fundamental concepts of Python programming.", parent_id=parent_skill.id),
            Skill(name="Statistics", description="The discipline that concerns the collection, organization, analysis, interpretation, and presentation of data.", parent_id=parent_skill.id),
            Skill(name="Machine Learning", description="A method of data analysis that automates analytical model building.", parent_id=parent_skill.id)
        ]
        
        for subskill in subskills:
            db.add(subskill)
        
        db.commit()
        
        # Create AI sub-skills
        ai_skill = db.query(Skill).filter(Skill.name == "Artificial Intelligence").first()
        
        ai_subskills = [
            Skill(name="Natural Language Processing", description="A field of AI that gives computers the ability to understand text and spoken words.", parent_id=ai_skill.id),
            Skill(name="Computer Vision", description="A field of AI that enables computers to derive meaningful information from digital images and videos.", parent_id=ai_skill.id),
            Skill(name="Reinforcement Learning", description="A type of machine learning where an agent learns to make decisions by taking actions in an environment.", parent_id=ai_skill.id)
        ]
        
        for subskill in ai_subskills:
            db.add(subskill)
        
        db.commit()
          # Create resources
        python_skill = db.query(Skill).filter(Skill.name == "Python Basics").first()
        
        resources = [
            Resource(
                title="Python.org Getting Started",
                url="https://www.python.org/about/gettingstarted/",
                description="Official Python getting started guide",
                resource_type="documentation",
                skill_id=python_skill.id
            ),
            Resource(
                title="Python Crash Course Video",
                url="https://www.youtube.com/watch?v=JJmcL1N2KQs",
                description="A 4-hour crash course on Python",
                resource_type="video",
                skill_id=python_skill.id
            ),
            Resource(
                title="Python Practice Exercises",
                url="https://github.com/zhiwehu/Python-programming-exercises",
                description="100+ Python exercises with solutions",
                resource_type="github",
                skill_id=python_skill.id
            )        ]
        
        # Add resources only if they don't exist (check by URL to avoid duplicates)
        for resource_data in resources:
            existing = db.query(Resource).filter(Resource.url == resource_data.url).first()
            if not existing:
                db.add(resource_data)
            else:
                print(f"  - Skipped duplicate resource: {resource_data.title}")
        
        db.commit()
        
        # Create progress for test user
        progress = SkillProgress(
            user_id=test_user.id,
            skill_id=python_skill.id,
            progress_percentage=25.0,
            completed=False
        )
        
        db.add(progress)
        db.commit()
        
        print("Sample data seeded successfully.")
    
    finally:
        db.close()

if __name__ == "__main__":
    import sys
    force = len(sys.argv) > 1 and sys.argv[1].lower() == "force"
    
    print(f"Starting data seeding process{' with force option' if force else ''}...")
    try:
        seed_data(force=force)
        print("Data seeding completed successfully.")
        sys.exit(0)
    except Exception as e:
        import traceback
        print(f"Error during data seeding: {e}")
        traceback.print_exc()
        print("Data seeding failed.")
        sys.exit(1)
