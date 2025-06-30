"""
Simple data seeding script for SkillSprint
Creates sample data for testing and demonstration
"""
import sys
import os
sys.path.append('.')

from sqlalchemy.orm import Session
from database.database import SessionLocal
from models.models import User, Skill, Resource, SkillProgress, XPTransaction

def create_sample_data():
    """Create sample data for the application"""
    db = SessionLocal()
    
    try:
        # Check if data already exists
        if db.query(User).count() > 0:
            print("✅ Data already exists in database")
            return True
            
        print("🌱 Creating sample data...")
        
        # Create a test user with simple password hash
        test_user = User(
            email="test@example.com",
            username="testuser",
            hashed_password="$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",  # secret: password123
            total_xp=150,
            current_streak=3,
            longest_streak=7
        )
        db.add(test_user)
        db.flush()  # Get the user ID
        
        print("👤 Created test user: testuser (password: password123)")
        
        # Create main skills
        skills_data = [
            {"name": "Data Science", "description": "The field of study that combines domain expertise, programming skills, and knowledge of mathematics and statistics."},
            {"name": "Web Development", "description": "The work involved in developing websites and web applications."},
            {"name": "Mobile Development", "description": "Creating applications for mobile devices like smartphones and tablets."},
            {"name": "Artificial Intelligence", "description": "The simulation of human intelligence processes by machines."},
            {"name": "DevOps", "description": "Practices that combine software development and IT operations."},
            {"name": "Cloud Computing", "description": "The delivery of computing services over the internet."}
        ]
        
        skills = []
        for skill_data in skills_data:
            skill = Skill(**skill_data)
            db.add(skill)
            skills.append(skill)
        
        db.flush()  # Get skill IDs
        print(f"🎯 Created {len(skills)} main skills")
        
        # Create sub-skills for Data Science
        data_science_skill = next(s for s in skills if s.name == "Data Science")
        subskills_data = [
            {"name": "Python Programming", "description": "Learn Python fundamentals for data science", "parent_id": data_science_skill.id},
            {"name": "Statistics & Math", "description": "Statistical concepts and mathematical foundations", "parent_id": data_science_skill.id},
            {"name": "Data Visualization", "description": "Creating charts and visualizations from data", "parent_id": data_science_skill.id},
            {"name": "Machine Learning", "description": "Algorithms that learn from data", "parent_id": data_science_skill.id}
        ]
        
        subskills = []
        for subskill_data in subskills_data:
            subskill = Skill(**subskill_data)
            db.add(subskill)
            subskills.append(subskill)
        
        db.flush()
        print(f"📚 Created {len(subskills)} sub-skills for Data Science")
        
        # Create sample resources
        python_skill = next(s for s in subskills if s.name == "Python Programming")
        resources_data = [
            {
                "title": "Python.org Official Tutorial",
                "url": "https://docs.python.org/3/tutorial/",
                "description": "The official Python tutorial covering all basics",
                "resource_type": "documentation",
                "skill_id": python_skill.id
            },
            {
                "title": "Python for Data Science Handbook",
                "url": "https://jakevdp.github.io/PythonDataScienceHandbook/",
                "description": "Essential tools for working with data in Python",
                "resource_type": "book",
                "skill_id": python_skill.id
            },
            {
                "title": "Codecademy Python Course",
                "url": "https://www.codecademy.com/learn/learn-python-3",
                "description": "Interactive Python programming course",
                "resource_type": "course",
                "skill_id": python_skill.id
            }
        ]
        
        for resource_data in resources_data:
            resource = Resource(**resource_data)
            db.add(resource)
        
        print(f"📖 Created {len(resources_data)} resources")
        
        # Create sample progress for the test user
        progress_data = [
            {"user_id": test_user.id, "skill_id": python_skill.id, "progress_percentage": 35.0, "completed": False},
            {"user_id": test_user.id, "skill_id": data_science_skill.id, "progress_percentage": 15.0, "completed": False}
        ]
        
        for progress_item in progress_data:
            progress = SkillProgress(**progress_item)
            db.add(progress)
        
        print(f"📊 Created progress tracking for {len(progress_data)} skills")
        
        # Create sample XP transactions
        xp_transactions = [
            {"user_id": test_user.id, "amount": 50, "transaction_type": "complete_subskill", "description": "Completed Python Basics", "skill_id": python_skill.id},
            {"user_id": test_user.id, "amount": 25, "transaction_type": "quiz_bonus", "description": "Quiz completed with 90% score", "skill_id": python_skill.id},
            {"user_id": test_user.id, "amount": 75, "transaction_type": "streak_bonus", "description": "7-day learning streak bonus"},
        ]
        
        for xp_data in xp_transactions:
            xp = XPTransaction(**xp_data)
            db.add(xp)
        
        print(f"🏆 Created {len(xp_transactions)} XP transactions")
        
        # Commit all changes
        db.commit()
        
        print("\n✅ Sample data created successfully!")
        print("\n📋 Test Account:")
        print("   Username: testuser")
        print("   Password: password123")
        print("   Email: test@example.com")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating sample data: {e}")
        db.rollback()
        return False
        
    finally:
        db.close()

if __name__ == "__main__":
    print("🚀 SkillSprint Data Seeding")
    print("=" * 30)
    
    if create_sample_data():
        print("\n🎉 Data seeding completed successfully!")
        print("You can now use the application with the test account.")
    else:
        print("\n💥 Data seeding failed!")
        sys.exit(1)
