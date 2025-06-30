"""
Simple test script to verify CORS and API functionality
"""
import requests
import json

def test_backend():
    base_url = "http://localhost:8000"
    
    print("🧪 Testing SkillSprint Backend API")
    print("=" * 40)
    
    # Test root endpoint
    try:
        response = requests.get(f"{base_url}/")
        print(f"✅ Root endpoint: {response.status_code}")
        print(f"   Response: {response.json()['message']}")
    except Exception as e:
        print(f"❌ Root endpoint failed: {e}")
        return False
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/health")
        print(f"✅ Health endpoint: {response.status_code}")
        print(f"   Status: {response.json()['status']}")
    except Exception as e:
        print(f"❌ Health endpoint failed: {e}")
    
    # Test CORS preflight
    try:
        headers = {
            'Origin': 'http://localhost:3000',
            'Access-Control-Request-Method': 'POST',
            'Access-Control-Request-Headers': 'Content-Type'
        }
        response = requests.options(f"{base_url}/auth/token", headers=headers)
        print(f"✅ CORS preflight: {response.status_code}")
        cors_header = response.headers.get('Access-Control-Allow-Origin', 'Not found')
        print(f"   CORS header: {cors_header}")
    except Exception as e:
        print(f"❌ CORS preflight failed: {e}")
    
    # Test auth endpoint (should fail without credentials, but should respond)
    try:
        data = {"username": "test", "password": "test"}
        response = requests.post(f"{base_url}/auth/token", data=data)
        print(f"✅ Auth endpoint responding: {response.status_code}")
        if response.status_code == 401:
            print("   Expected 401 (unauthorized) response")
    except Exception as e:
        print(f"❌ Auth endpoint failed: {e}")

if __name__ == "__main__":
    test_backend()
