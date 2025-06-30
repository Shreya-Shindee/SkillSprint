"""
Quick Demo Starter for SkillSprint
Run this script to start the development environment with demo data ready
"""

import subprocess
import sys
import os
from create_demo_users import print_demo_credentials

def start_demo():
    """Start the SkillSprint demo environment"""
    
    print("🚀 Starting SkillSprint Demo Environment...")
    print("="*60)
    
    # Print demo credentials
    print_demo_credentials()
    
    print("🔧 Starting backend server...")
    print("Server will be available at: http://localhost:8000")
    print("API documentation at: http://localhost:8000/docs")
    print()
    print("📱 Don't forget to start the frontend:")
    print("   cd ../frontend")
    print("   npm start")
    print()
    print("="*60)
    print("🎯 Ready to test! Use the demo credentials above to login.")
    print("="*60)
    
    # Start the FastAPI server
    try:
        subprocess.run([sys.executable, "-m", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"])
    except KeyboardInterrupt:
        print("\n👋 Demo environment stopped. Thanks for testing SkillSprint!")

if __name__ == "__main__":
    start_demo()
