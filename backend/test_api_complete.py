#!/usr/bin/env python3
"""
Test SkillSprint API endpoints
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_api():
    print("🧪 Testing SkillSprint API...")
    
    # Test 1: Check if API is running
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            print("✅ API is running")
            data = response.json()
            print(f"   Status: {data.get('status')}")
        else:
            print(f"❌ API not responding (status: {response.status_code})")
            return False
    except Exception as e:
        print(f"❌ Cannot connect to API: {e}")
        return False
    
    # Test 2: Login with demo user
    try:
        login_data = {
            "username": "testuser",
            "password": "password123"
        }
        response = requests.post(
            f"{BASE_URL}/auth/token",
            data=login_data,
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        
        if response.status_code == 200:
            print("✅ Demo user login successful")
            token_data = response.json()
            access_token = token_data.get("access_token")
            print(f"   Token type: {token_data.get('token_type')}")
            
            # Test 3: Access protected endpoint
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get(f"{BASE_URL}/users/me", headers=headers)
            
            if response.status_code == 200:
                print("✅ Protected endpoint access successful")
                user_data = response.json()
                print(f"   User: {user_data.get('username')} ({user_data.get('email')})")
            else:
                print(f"❌ Protected endpoint failed (status: {response.status_code})")
        else:
            print(f"❌ Demo user login failed (status: {response.status_code})")
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Login test failed: {e}")
    
    # Test 4: Skills endpoint
    try:
        response = requests.get(f"{BASE_URL}/skills/")
        if response.status_code == 200:
            skills = response.json()
            print(f"✅ Skills endpoint working ({len(skills)} skills available)")
        else:
            print(f"❌ Skills endpoint failed (status: {response.status_code})")
    except Exception as e:
        print(f"❌ Skills test failed: {e}")
    
    print("\n🎯 API tests completed!")

if __name__ == "__main__":
    test_api()
