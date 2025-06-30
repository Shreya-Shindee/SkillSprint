#!/usr/bin/env python3
"""Test script to verify DSA resource injection"""

from utils.resource_search import get_resources_for_skill

def test_dsa_resources():
    print("Testing DSA resource injection...")
    
    # Main DSA skills - should include Striver's sheet
    main_dsa_skills = [
        "data structure and algorithm",
        "data structures and algorithms",
        "dsa"
    ]
    
    # DSA subskills - should NOT include Striver's sheet (to avoid repetition)
    dsa_subskills = [
        "arrays",
        "linked lists", 
        "binary trees",
        "sorting algorithms",
        "dynamic programming"
    ]
    
    print("\n🎯 MAIN DSA SKILLS (should include Striver's sheet):")
    for skill in main_dsa_skills:
        print(f"\n=== Testing skill: '{skill}' ===")
        resources = get_resources_for_skill(skill, max_per_type=3)
        print(f"Found {len(resources)} resources")
        
        # Check if Striver's DSA Sheet is included
        striver_found = False
        for resource in resources:
            print(f"- {resource['title']} (Quality: {resource['quality_score']})")
            if "Striver" in resource['title']:
                striver_found = True
                print("  ✅ Striver's DSA Sheet found!")
        
        if not striver_found:
            print("  ❌ Striver's DSA Sheet NOT found")
    
    print("\n🔍 DSA SUBSKILLS (should NOT include Striver's sheet):")
    for skill in dsa_subskills:
        print(f"\n=== Testing subskill: '{skill}' ===")
        resources = get_resources_for_skill(skill, max_per_type=3)
        print(f"Found {len(resources)} resources")
        
        # Check if Striver's DSA Sheet is included (should not be)
        striver_found = False
        for resource in resources:
            print(f"- {resource['title']} (Quality: {resource['quality_score']})")
            if "Striver" in resource['title']:
                striver_found = True
                print("  ❌ Striver's DSA Sheet found (should NOT be here!)")
        
        if not striver_found:
            print("  ✅ Striver's DSA Sheet correctly NOT included")

if __name__ == "__main__":
    test_dsa_resources()
