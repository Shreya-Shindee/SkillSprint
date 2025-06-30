"""
Demo User Setup for SkillSprint Testing
This file creates demo users with predefined credentials for easy testing.
"""

from sqlalchemy.orm import Session
from database.database import SessionLocal
from models.models import User, Skill, Resource, SkillProgress, XPTransaction
from utils.auth import get_password_hash
import random

def create_demo_users():
    """Create demo users with realistic data for testing"""
    db = SessionLocal()
    
    try:
        # Check if demo users already exist
        existing_demo = db.query(User).filter(User.email.like("%demo%")).first()
        if existing_demo:
            print("Demo users already exist. Skipping creation.")
            print_demo_credentials()
            return
        
        print("Creating demo users...")
        
        # Demo Users with different progress levels
        demo_users = [
            {
                "email": "demo@skillsprint.com",
                "username": "demo",
                "password": "demo123",
                "xp_amount": 1250
            },
            {
                "email": "sarah.demo@skillsprint.com", 
                "username": "sarah_demo",
                "password": "sarah123",
                "xp_amount": 2450
            },
            {
                "email": "alex.demo@skillsprint.com",
                "username": "alex_demo", 
                "password": "alex123",
                "xp_amount": 750
            },
            {
                "email": "admin@skillsprint.com",
                "username": "admin",
                "password": "admin123",
                "xp_amount": 5000
            }
        ]
        
        created_users = []
        
        for user_data in demo_users:
            # Create user
            user = User(
                email=user_data["email"],
                username=user_data["username"],
                hashed_password=get_password_hash(user_data["password"])
            )
            db.add(user)
            db.commit()
            db.refresh(user)
            created_users.append(user)
            
            # Add initial XP transaction
            initial_xp = XPTransaction(
                user_id=user.id,
                amount=user_data["xp_amount"],
                description="Initial demo user XP"
            )
            db.add(initial_xp)
            
            # Add some random XP transactions for realistic data
            for i in range(random.randint(2, 5)):
                xp_transaction = XPTransaction(
                    user_id=user.id,
                    amount=random.randint(25, 200),
                    description=f"Completed skill module {i+1}"
                )
                db.add(xp_transaction)
        
        db.commit()
        print(f"✅ Successfully created {len(created_users)} demo users!")
        print_demo_credentials()
        
    except Exception as e:
        print(f"❌ Error creating demo users: {e}")
        db.rollback()
    finally:
        db.close()

def print_demo_credentials():
    """Print demo user credentials for easy reference"""
    print("\n" + "="*60)
    print("🎯 DEMO USER CREDENTIALS FOR TESTING")
    print("="*60)
    print("1. Main Demo User:")
    print("   Email: demo@skillsprint.com")
    print("   Username: demo") 
    print("   Password: demo123")
    print("   XP: 1250+")
    print()
    print("2. Advanced User (Sarah):")
    print("   Email: sarah.demo@skillsprint.com")
    print("   Username: sarah_demo")
    print("   Password: sarah123")
    print("   XP: 2450+")
    print()
    print("3. Beginner User (Alex):")
    print("   Email: alex.demo@skillsprint.com") 
    print("   Username: alex_demo")
    print("   Password: alex123")
    print("   XP: 750+")
    print()
    print("4. Admin User:")
    print("   Email: admin@skillsprint.com")
    print("   Username: admin")
    print("   Password: admin123")
    print("   XP: 5000+")
    print("="*60)
    print("💡 Use any of these credentials to test the login functionality!")
    print("="*60 + "\n")

if __name__ == "__main__":
    create_demo_users()
