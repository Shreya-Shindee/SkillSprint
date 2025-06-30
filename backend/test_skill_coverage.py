#!/usr/bin/env python3
"""
Test script to verify resource coverage for various skill domains.
"""

import sys
import os

# Add backend to path
backend_path = os.path.join(os.path.dirname(__file__))
if backend_path not in sys.path:
    sys.path.append(backend_path)

from utils.resource_search import get_resources_for_skill

def test_skill_resources(skill_name, expected_unique=True):
    """Test that a skill gets unique, relevant resources."""
    print(f"\n=== Testing: {skill_name} ===")
    
    try:
        resources = get_resources_for_skill(skill_name, max_per_type=2, resource_types=['article', 'video'])
        
        print(f"Found {len(resources)} resources:")
        
        urls = []
        for i, resource in enumerate(resources, 1):
            title = resource.get('title', 'Unknown')
            url = resource.get('url', 'No URL')
            description = resource.get('description', 'No description')
            quality = resource.get('quality_score', 0)
            
            print(f"{i}. {title}")
            print(f"   URL: {url}")
            print(f"   Description: {description}")
            print(f"   Quality Score: {quality}")
            print()
            
            urls.append(url)
        
        # Check for duplicates
        unique_urls = set(urls)
        if len(urls) != len(unique_urls):
            print(f"⚠️  WARNING: Found duplicate URLs for {skill_name}")
            duplicates = [url for url in urls if urls.count(url) > 1]
            print(f"   Duplicates: {set(duplicates)}")
        else:
            print(f"✅ All URLs are unique for {skill_name}")
            
        # Check relevance (simple heuristic)
        skill_words = skill_name.lower().split()
        relevant_count = 0
        for resource in resources:
            title_desc = (resource.get('title', '') + ' ' + resource.get('description', '')).lower()
            if any(word in title_desc for word in skill_words):
                relevant_count += 1
                
        print(f"📊 Relevance: {relevant_count}/{len(resources)} resources contain skill keywords")
        
        return resources
        
    except Exception as e:
        print(f"❌ Error testing {skill_name}: {e}")
        return []

if __name__ == "__main__":
    # Test various skill domains beyond DSA
    test_skills = [
        # Backend/API Development
        "REST API Development",
        "FastAPI",
        "Express.js",
        "Django",
        "Flask",
        
        # Frontend Frameworks
        "Vue.js",
        "Angular",
        "Svelte",
        "Next.js",
        
        # Mobile Development
        "React Native",
        "Flutter", 
        "iOS Development",
        "Android Development",
        
        # DevOps/Cloud
        "Docker",
        "Kubernetes",
        "AWS",
        "Azure",
        "CI/CD",
        
        # Databases
        "PostgreSQL",
        "MongoDB",
        "Redis",
        "SQL",
        
        # Design
        "UI/UX Design",
        "Figma",
        "Adobe Photoshop",
        
        # Business/Soft Skills
        "Project Management",
        "Agile Methodology",
        "Public Speaking",
        
        # Data Science
        "Data Analysis",
        "Tableau",
        "Power BI",
        
        # Security
        "Cybersecurity",
        "Ethical Hacking",
        "Network Security"
    ]
    
    print("Testing resource coverage for various skill domains...")
    print("=" * 60)
    
    total_tested = 0
    successful_tests = 0
    
    for skill in test_skills:
        resources = test_skill_resources(skill)
        total_tested += 1
        if len(resources) > 0:
            successful_tests += 1
    
    print("\n" + "=" * 60)
    print(f"SUMMARY: {successful_tests}/{total_tested} skills returned resources")
    print(f"Success rate: {(successful_tests/total_tested)*100:.1f}%")
