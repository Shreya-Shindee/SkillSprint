#!/usr/bin/env python3
"""
Check and fix user password hashing
"""
import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from database.database import get_db
    from models.models import User
    from utils.auth import get_password_hash, verify_password
    
    # Create engine and session
    engine = create_engine('sqlite:///./skillsprint.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Get the test user
    user = session.query(User).filter(User.username == "testuser").first()
    
    if user:
        print(f"✅ Found user: {user.username}")
        print(f"📧 Email: {user.email}")
        print(f"🔑 Current hashed password: {user.hashed_password}")
        
        # Check if current password verifies
        try:
            test_verify = verify_password("password123", user.hashed_password)
            print(f"🔍 Password verification test: {test_verify}")
        except Exception as e:
            print(f"❌ Password verification failed: {e}")
            print("🔧 Re-hashing password...")
            
            # Re-hash the password properly
            new_hashed = get_password_hash("password123")
            user.hashed_password = new_hashed
            session.commit()
            
            print(f"✅ New hashed password: {new_hashed}")
            
            # Test again
            test_verify = verify_password("password123", user.hashed_password)
            print(f"🔍 New password verification test: {test_verify}")
    else:
        print("❌ Test user not found")
    
    session.close()
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
