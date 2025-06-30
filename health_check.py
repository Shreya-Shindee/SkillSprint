#!/usr/bin/env python3
"""
SkillSprint System Health Check
Verifies that all components are working correctly
"""

import sys
import os
import sqlite3
import requests
import time
from pathlib import Path

# Add the backend path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

def print_status(message, status="INFO"):
    """Print formatted status messages"""
    colors = {
        "INFO": "\033[94m",  # Blue
        "SUCCESS": "\033[92m",  # Green
        "WARNING": "\033[93m",  # Yellow
        "ERROR": "\033[91m",  # Red
        "RESET": "\033[0m"  # Reset
    }
    
    icon = {
        "INFO": "ℹ️",
        "SUCCESS": "✅",
        "WARNING": "⚠️",
        "ERROR": "❌"
    }
    
    print(f"{colors[status]}{icon[status]} {message}{colors['RESET']}")

def check_python_version():
    """Check Python version compatibility"""
    print_status("Checking Python version...")
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print_status(f"Python {version.major}.{version.minor}.{version.micro} - Compatible", "SUCCESS")
        return True
    else:
        print_status(f"Python {version.major}.{version.minor}.{version.micro} - Requires Python 3.8+", "ERROR")
        return False

def check_dependencies():
    """Check if required Python packages are installed"""
    print_status("Checking Python dependencies...")
    required_packages = [
        'fastapi',
        'uvicorn',
        'sqlalchemy',
        'pydantic',
        'python_jose',
        'passlib',
        'python_multipart',
        'sentence_transformers',
        'numpy',
        'requests'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print_status(f"  {package} - Installed", "SUCCESS")
        except ImportError:
            print_status(f"  {package} - Missing", "ERROR")
            missing_packages.append(package)
    
    if missing_packages:
        print_status(f"Missing packages: {', '.join(missing_packages)}", "ERROR")
        print_status("Run: pip install -r backend/requirements.txt", "INFO")
        return False
    else:
        print_status("All dependencies installed", "SUCCESS")
        return True

def check_database():
    """Check database connection and structure"""
    print_status("Checking database...")
    db_path = Path("backend/skillsprint.db")
    
    if not db_path.exists():
        print_status("Database file not found", "WARNING")
        print_status("Run: python -c \"from database.init_db import init_database; init_database()\"", "INFO")
        return False
    
    try:
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        
        # Check if main tables exist
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
        
        required_tables = ['users', 'skills', 'learning_paths', 'quizzes', 'user_progress']
        missing_tables = [table for table in required_tables if table not in tables]
        
        if missing_tables:
            print_status(f"Missing tables: {', '.join(missing_tables)}", "WARNING")
            print_status("Database needs initialization", "INFO")
            conn.close()
            return False
        else:
            print_status(f"Database has {len(tables)} tables", "SUCCESS")
            conn.close()
            return True
            
    except Exception as e:
        print_status(f"Database error: {str(e)}", "ERROR")
        return False

def check_backend_server():
    """Check if backend server is running"""
    print_status("Checking backend server...")
    try:
        response = requests.get("http://localhost:8000/health", timeout=5)
        if response.status_code == 200:
            print_status("Backend server is running", "SUCCESS")
            print_status(f"Response: {response.json()}", "INFO")
            return True
        else:
            print_status(f"Backend server returned status {response.status_code}", "WARNING")
            return False
    except requests.exceptions.ConnectionError:
        print_status("Backend server is not running", "WARNING")
        print_status("Start with: python backend/main.py", "INFO")
        return False
    except Exception as e:
        print_status(f"Backend check error: {str(e)}", "ERROR")
        return False

def check_frontend():
    """Check if frontend is accessible"""
    print_status("Checking frontend...")
    try:
        response = requests.get("http://localhost:3000", timeout=5)
        if response.status_code == 200:
            print_status("Frontend is running", "SUCCESS")
            return True
        else:
            print_status(f"Frontend returned status {response.status_code}", "WARNING")
            return False
    except requests.exceptions.ConnectionError:
        print_status("Frontend is not running", "WARNING")
        print_status("Start with: cd frontend && npm start", "INFO")
        return False
    except Exception as e:
        print_status(f"Frontend check error: {str(e)}", "ERROR")
        return False

def check_environment_config():
    """Check environment configuration"""
    print_status("Checking environment configuration...")
    
    # Check backend .env
    backend_env = Path("backend/.env")
    if backend_env.exists():
        print_status("Backend .env file found", "SUCCESS")
    else:
        print_status("Backend .env file missing", "WARNING")
        print_status("Copy from backend/.env.example", "INFO")
        return False
    
    # Check frontend .env
    frontend_env = Path("frontend/.env.development")
    if frontend_env.exists():
        print_status("Frontend .env.development file found", "SUCCESS")
    else:
        print_status("Frontend .env.development file missing", "WARNING")
        return False
    
    return True

def main():
    """Run all health checks"""
    print("🔍 SkillSprint System Health Check")
    print("=" * 40)
    
    checks = [
        ("Python Version", check_python_version),
        ("Dependencies", check_dependencies),
        ("Environment Config", check_environment_config),
        ("Database", check_database),
        ("Backend Server", check_backend_server),
        ("Frontend", check_frontend),
    ]
    
    results = {}
    for check_name, check_func in checks:
        print(f"\n📋 {check_name}")
        print("-" * 20)
        results[check_name] = check_func()
    
    # Summary
    print("\n📊 Health Check Summary")
    print("=" * 40)
    
    passed = sum(results.values())
    total = len(results)
    
    for check_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{check_name:20} {status}")
    
    print(f"\nOverall: {passed}/{total} checks passed")
    
    if passed == total:
        print_status("🎉 All systems operational!", "SUCCESS")
        print_status("Ready to run SkillSprint!", "SUCCESS")
        return 0
    else:
        print_status("⚠️ Some issues found", "WARNING")
        print_status("Please resolve the issues above", "INFO")
        return 1

if __name__ == "__main__":
    sys.exit(main())
