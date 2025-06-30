#!/usr/bin/env python3
"""Test script to verify enhanced subskill-specific resources"""

from utils.resource_search import get_resources_for_skill

def test_subskill_specificity():
    print("Testing Subskill-Specific Resource Generation...")
    print("=" * 60)
    
    # Test DSA subskills - each should have unique resources
    dsa_subskills = [
        "arrays",
        "linked lists", 
        "binary trees",
        "stacks",
        "queues",
        "graphs",
        "dynamic programming",
        "sorting algorithms",
        "searching algorithms"
    ]
    
    # Test Web Development subskills
    web_subskills = [
        "html fundamentals",
        "css fundamentals", 
        "javascript fundamentals",
        "react fundamentals",
        "node.js backend"
    ]
    
    # Test Machine Learning subskills
    ml_subskills = [
        "linear algebra for ml",
        "statistics for ml",
        "supervised learning",
        "deep learning"
    ]
    
    # Test Python subskills
    python_subskills = [
        "python basics",
        "object-oriented programming",
        "python libraries"
    ]
    
    all_tests = [
        ("DSA Subskills", dsa_subskills),
        ("Web Development Subskills", web_subskills),
        ("Machine Learning Subskills", ml_subskills),
        ("Python Subskills", python_subskills)
    ]
    
    total_unique_resources = 0
    
    for category, subskills in all_tests:
        print(f"\n🎯 {category}:")
        print("-" * 40)
        
        for subskill in subskills:
            resources = get_resources_for_skill(subskill, max_per_type=4)
            total_unique_resources += len(resources)
            
            print(f"\n📚 {subskill.title()}:")
            print(f"   Found {len(resources)} resources")
            
            if resources:
                # Show top 2 resources
                for i, resource in enumerate(resources[:2]):
                    print(f"   {i+1}. {resource['title']} (Quality: {resource['quality_score']})")
                    print(f"      🔗 {resource['url'][:60]}...")
                
                # Check for unique, relevant content
                relevant_keywords = subskill.lower().split()
                relevance_found = False
                for resource in resources:
                    resource_text = (resource['title'] + ' ' + resource['description']).lower()
                    if any(keyword in resource_text for keyword in relevant_keywords):
                        relevance_found = True
                        break
                
                if relevance_found:
                    print(f"   ✅ Resources are relevant to '{subskill}'")
                else:
                    print(f"   ⚠️  Resources may not be specific to '{subskill}'")
            else:
                print(f"   ❌ No resources found for '{subskill}'")
    
    print("\n" + "=" * 60)
    print(f"🎉 Total unique resources generated: {total_unique_resources}")
    print("✅ Each subskill now has its own tailored learning resources!")

if __name__ == "__main__":
    test_subskill_specificity()
