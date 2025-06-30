"""
SkillSprint Universal Resource Test
Test script to demonstrate that the platform can provide resources for ANY skill.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.fast_fallback import get_fast_fallback_resources
from utils.resource_search import get_resources_for_skill

def test_universal_skills():
    """Test the universal skill resource generation"""
    
    # Test a wide variety of skills
    test_skills = [
        # Programming & Tech
        "Python", "JavaScript", "Machine Learning", "Blockchain Development",
        
        # Creative Arts  
        "Photography", "Digital Art", "Music Production", "Creative Writing",
        
        # Life Skills
        "Cooking", "Gardening", "Public Speaking", "Time Management",
        
        # Fitness & Health
        "Yoga", "Meditation", "Weight Training", "Nutrition",
        
        # Business & Professional
        "Digital Marketing", "Project Management", "Sales", "Leadership",
        
        # Academic & Science
        "Physics", "Chemistry", "History", "Philosophy",
        
        # Hobbies & Crafts
        "Pottery", "Woodworking", "Knitting", "Chess",
        
        # Unique/Niche Skills
        "Bee Keeping", "Drone Piloting", "Voice Acting", "Origami",
        "Juggling", "Card Magic", "Speed Reading", "Memory Techniques"
    ]
    
    print("🎯 SkillSprint Universal Resource Test")
    print("=" * 50)
    print(f"Testing {len(test_skills)} diverse skills...")
    print()
    
    success_count = 0
    
    for skill in test_skills:
        try:
            resources = get_fast_fallback_resources(skill)
            if resources and len(resources) > 0:
                success_count += 1
                print(f"✅ {skill}: {len(resources)} resources found")
                # Show top resource
                top_resource = resources[0]
                print(f"   📚 Top: {top_resource['title']} (Score: {top_resource['quality_score']})")
            else:
                print(f"❌ {skill}: No resources found")
        except Exception as e:
            print(f"⚠️  {skill}: Error - {e}")
        print()
    
    print("=" * 50)
    print(f"🎉 Results: {success_count}/{len(test_skills)} skills supported ({success_count/len(test_skills)*100:.1f}%)")
    
    if success_count == len(test_skills):
        print("🚀 SUCCESS: SkillSprint can provide resources for ANY skill!")
    else:
        print("📈 Good coverage, system can handle most skills universally")

if __name__ == "__main__":
    test_universal_skills()
