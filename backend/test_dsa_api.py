#!/usr/bin/env python3
"""Test script to verify DSA resource injection via API"""

import requests
import json

def test_dsa_api():
    base_url = "http://localhost:8000"
    
    # Test data for authentication
    test_user = {
        "username": "demo",
        "password": "demo123"
    }
    
    print("Testing DSA resource injection via API...")
    
    try:
        # First, try to login to get a token
        login_data = {
            "username": test_user["username"],
            "password": test_user["password"]
        }
        
        print("1. Attempting to login...")
        login_response = requests.post(f"{base_url}/auth/token", data=login_data)
        
        if login_response.status_code == 200:
            token = login_response.json()["access_token"]
            headers = {"Authorization": f"Bearer {token}"}
            print("✅ Login successful")
        else:
            print("❌ Login failed, testing without authentication")
            headers = {}
    
    except Exception as e:
        print(f"❌ Server not running or login failed: {e}")
        print("Please start the backend server first")
        return
    
    # Test DSA resource endpoint
    test_skills = ["data structure and algorithm", "data structures", "algorithms"]
    
    for skill in test_skills:
        print(f"\n=== Testing skill: '{skill}' ===")
        try:
            # Test the resource endpoint
            resource_data = {"skill_name": skill}
            response = requests.post(
                f"{base_url}/resources/by-skill-name", 
                json=resource_data,
                headers=headers
            )
            
            if response.status_code == 200:
                data = response.json()
                resources = data.get(skill, [])
                print(f"Found {len(resources)} resources via API")
                
                # Check if Striver's DSA Sheet is included
                striver_found = False
                for resource in resources[:3]:  # Show top 3
                    print(f"- {resource['title']} (Quality: {resource.get('quality_score', 'N/A')})")
                    if "Striver" in resource['title']:
                        striver_found = True
                        print("  ✅ Striver's DSA Sheet found via API!")
                
                if not striver_found:
                    print("  ❌ Striver's DSA Sheet NOT found via API")
            else:
                print(f"❌ API request failed: {response.status_code}")
                print(response.text)
                
        except Exception as e:
            print(f"❌ Error testing skill '{skill}': {e}")

if __name__ == "__main__":
    test_dsa_api()
