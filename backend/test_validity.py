#!/usr/bin/env python3
"""
Simple test to verify all resources are valid and high-quality
"""
import sys
sys.path.append('.')

from utils.enhanced_uniqueness import get_specialized_resources_for_subskill, validate_url_accessibility

def test_resource_validity():
    print("🔍 Testing Resource Validity")
    print("=" * 50)
    
    # Test specialized resources for Arrays
    print("Testing Arrays resources...")
    array_resources = get_specialized_resources_for_subskill("Arrays")
    
    all_valid = True
    for i, resource in enumerate(array_resources, 1):
        url = resource.get('url', '')
        title = resource.get('title', 'No title')
        
        print(f"  {i}. {title}")
        print(f"     URL: {url}")
        
        # Test if URL is valid
        is_valid = validate_url_accessibility(url)
        if is_valid:
            print(f"     ✅ Valid (Quality: {resource.get('quality_score', 0)})")
        else:
            print(f"     ❌ INVALID!")
            all_valid = False
        print()
    
    if all_valid:
        print("🎉 All resources are valid and accessible!")
    else:
        print("⚠️  Some resources need to be fixed!")

if __name__ == "__main__":
    test_resource_validity()
