#!/usr/bin/env python3
"""
Test script to verify the robust resource fetcher handles API limitations correctly.
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.robust_resource_fetcher import get_robust_resources
from utils.resource_search import get_resources_for_skill
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def test_robust_fetcher():
    """Test the robust resource fetcher with different subskills."""
    
    test_subskills = [
        "Arrays",
        "Linked Lists", 
        "Binary Trees",
        "Dynamic Programming",
        "JavaScript Fundamentals",
        "React Fundamentals",
        "Machine Learning"
    ]
    
    print("🔍 Testing Robust Resource Fetcher")
    print("=" * 50)
    
    for subskill in test_subskills:
        print(f"\n📚 Testing: {subskill}")
        print("-" * 30)
        
        try:
            # Test robust fetcher directly
            robust_resources = get_robust_resources(subskill, max_per_type=3)
            print(f"✅ Robust Fetcher: Got {len(robust_resources)} resources")
            
            # Show resource types
            resource_types = {}
            for resource in robust_resources:
                rtype = resource.get('resource_type', 'unknown')
                resource_types[rtype] = resource_types.get(rtype, 0) + 1
            
            print(f"   Resource types: {dict(resource_types)}")
            
            # Test comprehensive search (which uses robust fetcher as fallback)
            comprehensive_resources = get_resources_for_skill(subskill)
            print(f"✅ Comprehensive Search: Got {len(comprehensive_resources)} resources")
            
            # Show comprehensive resource types
            comp_resource_types = {}
            for resource in comprehensive_resources:
                rtype = resource.get('resource_type', 'unknown')
                comp_resource_types[rtype] = comp_resource_types.get(rtype, 0) + 1
            
            print(f"   Resource types: {dict(comp_resource_types)}")
            
            # Quality check
            avg_quality = sum(r.get('quality_score', 50) for r in comprehensive_resources) / len(comprehensive_resources) if comprehensive_resources else 0
            print(f"   Average quality score: {avg_quality:.1f}")
            
        except Exception as e:
            print(f"❌ Error testing {subskill}: {e}")
    
    print("\n" + "=" * 50)
    print("✅ Robust Resource Fetcher Test Complete")

def test_api_fallback():
    """Test how the system handles API rate limiting."""
    
    print("\n🚫 Testing API Rate Limiting Fallback")
    print("=" * 50)
    
    # Test with a skill that might trigger rate limiting
    test_skill = "Python Programming"
    
    try:
        resources = get_resources_for_skill(test_skill)
        print(f"✅ Got {len(resources)} resources despite potential API limits")
        
        # Check diversity
        types = {}
        for resource in resources:
            rtype = resource.get('resource_type', 'unknown')
            types[rtype] = types.get(rtype, 0) + 1
        
        print(f"📊 Resource type distribution: {dict(types)}")
        
        # Show top 5 resources
        print("\n🏆 Top 5 Resources:")
        for i, resource in enumerate(resources[:5], 1):
            print(f"   {i}. {resource.get('title', 'Unknown')} ({resource.get('resource_type', 'unknown')}) - Quality: {resource.get('quality_score', 0)}")
    
    except Exception as e:
        print(f"❌ Error in API fallback test: {e}")

if __name__ == "__main__":
    test_robust_fetcher()
    test_api_fallback()
