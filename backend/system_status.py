#!/usr/bin/env python3
"""
SkillSprint System Status Check
"""
import requests
import sqlite3
import os

def check_system_status():
    print("🏥 SkillSprint System Health Check")
    print("================================")
    
    # 1. Database Check
    print("\n📊 Database Status:")
    try:
        db_path = "./skillsprint.db"
        if os.path.exists(db_path):
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Check users table
            cursor.execute("SELECT COUNT(*) FROM users")
            user_count = cursor.fetchone()[0]
            print(f"   ✅ Users: {user_count}")
            
            # Check skills table
            cursor.execute("SELECT COUNT(*) FROM skills")
            skill_count = cursor.fetchone()[0]
            print(f"   ✅ Skills: {skill_count}")
            
            # Check demo user
            cursor.execute("SELECT username, email FROM users WHERE username='testuser'")
            demo_user = cursor.fetchone()
            if demo_user:
                print(f"   ✅ Demo user: {demo_user[0]} ({demo_user[1]})")
            else:
                print("   ❌ Demo user not found")
            
            conn.close()
        else:
            print("   ❌ Database file not found")
    except Exception as e:
        print(f"   ❌ Database error: {e}")
    
    # 2. Backend API Check
    print("\n🔗 Backend API Status:")
    try:
        # Health check
        response = requests.get("http://localhost:8000/health", timeout=5)
        if response.status_code == 200:
            print("   ✅ Health endpoint: OK")
        else:
            print(f"   ❌ Health endpoint: {response.status_code}")
        
        # Authentication check
        login_data = "username=testuser&password=password123"
        response = requests.post(
            "http://localhost:8000/auth/token",
            data=login_data,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            timeout=5
        )
        if response.status_code == 200:
            print("   ✅ Authentication: OK")
        else:
            print(f"   ❌ Authentication: {response.status_code}")
        
        # Skills endpoint
        response = requests.get("http://localhost:8000/skills/", timeout=5)
        if response.status_code == 200:
            print("   ✅ Skills API: OK")
        else:
            print(f"   ❌ Skills API: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("   ❌ Backend not running")
    except Exception as e:
        print(f"   ❌ Backend error: {e}")
    
    # 3. Frontend Check
    print("\n🎨 Frontend Status:")
    try:
        response = requests.get("http://localhost:3001", timeout=10)
        if response.status_code == 200:
            print("   ✅ Frontend: Running on port 3001")
        else:
            print(f"   ❌ Frontend: {response.status_code}")
    except requests.exceptions.ConnectionError:
        # Try port 3000
        try:
            response = requests.get("http://localhost:3000", timeout=10)
            if response.status_code == 200:
                print("   ✅ Frontend: Running on port 3000")
            else:
                print(f"   ❌ Frontend: {response.status_code}")
        except:
            print("   ❌ Frontend not running")
    except Exception as e:
        print(f"   ❌ Frontend error: {e}")
    
    print("\n🔐 Demo Credentials:")
    print("   Username: testuser")
    print("   Password: password123")
    
    print("\n🌐 Access URLs:")
    print("   Frontend: http://localhost:3001 (or 3000)")
    print("   Backend API: http://localhost:8000")
    print("   API Docs: http://localhost:8000/docs")
    
    print("\n📋 Summary:")
    print("   - Backend: FastAPI with SQLite database")
    print("   - Frontend: React with Tailwind CSS")
    print("   - Authentication: JWT tokens with bcrypt")
    print("   - Features: AI-powered adaptive learning platform")

if __name__ == "__main__":
    check_system_status()
