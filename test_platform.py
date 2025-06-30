#!/usr/bin/env python3
"""
Quick test to verify the SkillSprint platform is working correctly
"""
import requests
import json
import time

# Configuration
BACKEND_URL = "http://localhost:8000"
FRONTEND_URL = "http://localhost:3000"

def test_backend():
    """Test backend functionality"""
    print("🔍 Testing Backend...")
    
    # Test health endpoint
    try:
        response = requests.get(f"{BACKEND_URL}/health", timeout=5)
        if response.status_code == 200:
            print("✅ Backend health check passed")
        else:
            print(f"❌ Backend health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Backend connection failed: {e}")
        return False
    
    # Test login
    try:
        login_data = {
            'username': 'testuser',
            'password': 'password123'
        }
        response = requests.post(f"{BACKEND_URL}/auth/token", data=login_data, timeout=5)
        if response.status_code == 200:
            print("✅ Demo user login successful")
            token = response.json().get('access_token')
            
            # Test authenticated endpoint
            headers = {'Authorization': f'Bearer {token}'}
            dashboard_response = requests.get(f"{BACKEND_URL}/dashboard/stats", headers=headers, timeout=5)
            if dashboard_response.status_code == 200:
                print("✅ Dashboard API endpoint working")
                print(f"   Stats: {dashboard_response.json()}")
            else:
                print(f"❌ Dashboard API failed: {dashboard_response.status_code}")
                return False
                
        else:
            print(f"❌ Demo user login failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Authentication test failed: {e}")
        return False
    
    return True

def test_frontend():
    """Test frontend accessibility"""
    print("\n🌐 Testing Frontend...")
    
    try:
        response = requests.get(FRONTEND_URL, timeout=10)
        if response.status_code == 200:
            print("✅ Frontend is accessible")
            if "SkillSprint" in response.text or "react" in response.text.lower():
                print("✅ Frontend contains expected content")
                return True
            else:
                print("⚠️ Frontend accessible but content unclear")
                return True
        else:
            print(f"❌ Frontend returned status: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Frontend connection failed: {e}")
        return False

def main():
    print("🚀 SkillSprint Platform Health Check")
    print("=" * 50)
    
    backend_ok = test_backend()
    frontend_ok = test_frontend()
    
    print("\n📊 Test Results:")
    print("=" * 50)
    
    if backend_ok and frontend_ok:
        print("🎉 All tests passed! SkillSprint platform is ready to use.")
        print(f"👉 Access the app at: {FRONTEND_URL}")
        print("👤 Demo user: testuser / password123")
        return True
    else:
        print("❌ Some tests failed. Please check the issues above.")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
