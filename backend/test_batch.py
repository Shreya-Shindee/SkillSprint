import requests
import json

auth_url = 'http://localhost:8000/auth/token'
auth_data = {'username': 'demo', 'password': 'demo123'}

try:
    auth_response = requests.post(auth_url, data=auth_data)
    if auth_response.status_code == 200:
        token = auth_response.json()['access_token']
        headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
        
        batch_url = 'http://localhost:8000/resources/search/batch'
        skills = ['Python Programming', 'Web Development', 'Machine Learning']
        
        response = requests.post(batch_url, json=skills, headers=headers)
        print(f'Status: {response.status_code}')
        result = response.json()
        print(f'Found resources for {result["total_skills"]} skills')
        for skill, resources in result['results'].items():
            print(f'  {skill}: {len(resources)} resources')
    else:
        print(f'Auth failed: {auth_response.status_code}')
except Exception as e:
    print(f'Error: {e}')
