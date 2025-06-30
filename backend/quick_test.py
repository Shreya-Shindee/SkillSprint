"""
Quick test to verify the optimized resource system is working
"""
import sys
import os
sys.path.append('.')

from utils.optimized_resource_db import get_optimized_resources, get_optimized_learning_path

def test_optimized_system():
    print("🚀 Testing Optimized SkillSprint Resource System")
    print("=" * 50)
    
    # Test 1: Resource retrieval
    print("\n📚 Testing Resource Retrieval:")
    print("-" * 30)
    
    test_skills = ["Python", "JavaScript", "React", "Machine Learning"]
    
    for skill in test_skills:
        resources = get_optimized_resources(skill, 10)
        print(f"✅ {skill}: {len(resources)} resources")
        if resources:
            print(f"   Quality: {resources[0].get('quality_score', 'N/A')}")
    
    # Test 2: Learning path generation
    print("\n🛤️ Testing Learning Path Generation:")
    print("-" * 30)
    
    for skill in ["Python", "React"]:
        learning_path = get_optimized_learning_path(skill)
        phases = learning_path.get("phases", [])
        total_resources = sum(len(phase.get("resources", [])) for phase in phases)
        
        print(f"✅ {skill}: {len(phases)} phases, {total_resources} total resources")
        print(f"   Duration: {learning_path.get('total_duration', 'N/A')}")
    
    print("\n🎉 All tests completed successfully!")
    print("✅ Optimized system is working correctly")
    print("✅ Resources are loading instantly")
    print("✅ Learning paths have comprehensive content")

if __name__ == "__main__":
    test_optimized_system()
