#!/usr/bin/env python3
"""
Quick script to check database state
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
    
    # Create engine and session
    engine = create_engine('sqlite:///./skillsprint.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    print(f"📍 Working directory: {os.getcwd()}")
    print(f"🗄️ Database file exists: {os.path.exists('skillsprint.db')}")
    
    # Check users
    users = session.query(User).all()
    print(f"👥 Users in database: {len(users)}")
    for user in users:
        print(f"   User: {user.username}, Email: {user.email}")
    
    # Check skills
    skills = session.query(Skill).all()
    print(f"🎯 Skills in database: {len(skills)}")
    for skill in skills[:5]:  # Show first 5
        print(f"   Skill: {skill.name}")
    
    session.close()
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
