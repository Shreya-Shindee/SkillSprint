#!/usr/bin/env python3
"""
Quick authentication test script
"""
import sys
sys.path.append('.')

from database.database import SessionLocal
from models.models import User
from utils.auth import get_password_hash, verify_password

def test_demo_user():
    """Test if demo user exists and can authenticate"""
    db = SessionLocal()
    
    try:
        # Check if demo user exists
        demo_user = db.query(User).filter(User.username == 'demo').first()
        
        if not demo_user:
            print("❌ Demo user 'demo' not found!")
            print("Creating demo user...")
            
            # Create demo user
            hashed_password = get_password_hash('demo123')
            demo_user = User(
                email='demo@skillsprint.com',
                username='demo',
                hashed_password=hashed_password
            )
            db.add(demo_user)
            db.commit()
            db.refresh(demo_user)
            print("✅ Demo user 'demo' created successfully!")
        else:
            print("✅ Demo user 'demo' found!")
        
        # Test password verification
        password_ok = verify_password('demo123', demo_user.hashed_password)
        if password_ok:
            print("✅ Password verification successful!")
        else:
            print("❌ Password verification failed!")
            
        print(f"📊 User details: ID={demo_user.id}, Email={demo_user.email}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    test_demo_user()
