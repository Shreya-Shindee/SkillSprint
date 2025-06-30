#!/usr/bin/env python3
"""
Frontend-Backend Integration Test
This script simulates frontend API calls to test the complete flow
"""
import requests
import json

def test_frontend_integration():
    print("🔗 Testing Frontend-Backend Integration...")
    
    # Simulate frontend login
    print("\n1. Testing Login Flow (as frontend would do)...")
    
    login_url = "http://localhost:8000/auth/token"
    login_data = "username=testuser&password=password123"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "http://localhost:3001"  # Simulate frontend origin
    }
    
    try:
        response = requests.post(login_url, data=login_data, headers=headers)
        if response.status_code == 200:
            print("   ✅ Login successful")
            token_data = response.json()
            access_token = token_data["access_token"]
            
            # Test protected endpoints with token
            auth_headers = {
                "Authorization": f"Bearer {access_token}",
                "Origin": "http://localhost:3001"
            }
            
            # Test user profile
            print("\n2. Testing User Profile...")
            response = requests.get("http://localhost:8000/users/me", headers=auth_headers)
            if response.status_code == 200:
                user = response.json()
                print(f"   ✅ User profile: {user['username']} ({user['email']})")
            else:
                print(f"   ❌ User profile failed: {response.status_code}")
            
            # Test skills
            print("\n3. Testing Skills API...")
            response = requests.get("http://localhost:8000/skills/", headers={"Origin": "http://localhost:3001"})
            if response.status_code == 200:
                skills = response.json()
                print(f"   ✅ Skills loaded: {len(skills)} skills")
                if skills:
                    print(f"   📚 Sample skill: {skills[0]['name']}")
            else:
                print(f"   ❌ Skills failed: {response.status_code}")
            
            # Test user registration (to verify the flow)
            print("\n4. Testing Registration Flow...")
            reg_data = {
                "username": "newuser",
                "email": "new@example.com", 
                "password": "newpassword123"
            }
            response = requests.post(
                "http://localhost:8000/auth/register",
                json=reg_data,
                headers={"Content-Type": "application/json", "Origin": "http://localhost:3001"}
            )
            if response.status_code == 200:
                print("   ✅ Registration flow working")
                # Clean up - delete the test user
                # (This would require admin privileges, so we'll skip cleanup for now)
            elif response.status_code == 400 and "already registered" in response.text:
                print("   ✅ Registration validation working (user already exists)")
            else:
                print(f"   ❌ Registration failed: {response.status_code} - {response.text}")
        
        else:
            print(f"   ❌ Login failed: {response.status_code} - {response.text}")
    
    except Exception as e:
        print(f"   ❌ Integration test failed: {e}")
    
    print("\n✨ Integration test completed!")
    print("\n🎯 Ready for frontend testing!")
    print("   👆 Go to http://localhost:3001 in your browser")
    print("   🔑 Login with: testuser / password123")

if __name__ == "__main__":
    test_frontend_integration()
