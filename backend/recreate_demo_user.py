#!/usr/bin/env python3
"""
Recreate demo user with proper password
"""
import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from database.database import get_db
    from models.models import User, Skill
    from utils.auth import get_password_hash, verify_password
    
    # Create engine and session
    engine = create_engine('sqlite:///./skillsprint.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Delete existing test user if exists
    existing_user = session.query(User).filter(User.username == "testuser").first()
    if existing_user:
        session.delete(existing_user)
        session.commit()
        print("🗑️ Deleted existing test user")
    
    # Create new demo user with proper password
    print("👤 Creating new demo user...")
    hashed_password = get_password_hash("password123")
    print(f"🔑 Generated hash: {hashed_password}")
    
    demo_user = User(
        username="testuser",
        email="test@example.com",
        hashed_password=hashed_password,
        is_active=True
    )
    
    session.add(demo_user)
    session.commit()
    session.refresh(demo_user)
    
    print(f"✅ Created user: {demo_user.username} (ID: {demo_user.id})")
    
    # Test password verification
    verification_result = verify_password("password123", demo_user.hashed_password)
    print(f"🔍 Password verification test: {verification_result}")
    
    if verification_result:
        print("✅ Demo user created successfully with working password!")
        print("📝 Login credentials:")
        print("   Username: testuser")
        print("   Password: password123")
    else:
        print("❌ Password verification failed")
    
    session.close()
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
