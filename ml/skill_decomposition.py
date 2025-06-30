import json
import numpy as np
import sys
import os

# Add parent directory to path to import utility functions
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.utils.resource_search import get_resources_for_skill as search_resources

# Handle potential import errors with sentence_transformers
try:
    from sentence_transformers import SentenceTransformer, util
    # Initialize the SentenceTransformer model
    # This will download the model the first time it's used
    model = SentenceTransformer('all-MiniLM-L6-v2')
    ML_AVAILABLE = True
except ImportError:
    print("Warning: sentence_transformers could not be imported. Using fallback methods.")
    model = None
    ML_AVAILABLE = False

# Sample skill hierarchy (can be expanded)
# Add additional skills to the hierarchy for better coverage
SKILL_HIERARCHY = {
    "Data Science": [
        "Python Basics", 
        "Statistics", 
        "Data Visualization", 
        "Machine Learning", 
        "Data Cleaning"
    ],
    "Python Basics": [
        "Variables", 
        "Data Types", 
        "Control Flow", 
        "Functions", 
        "OOP"
    ],
    "Machine Learning": [
        "Supervised Learning", 
        "Unsupervised Learning", 
        "Deep Learning", 
        "Model Evaluation"
    ],
    "Web Development": [
        "HTML", 
        "CSS", 
        "JavaScript", 
        "Frontend Frameworks", 
        "Backend Development"
    ],
    "Artificial Intelligence": [
        "Natural Language Processing",
        "Computer Vision",
        "Reinforcement Learning",
        "Neural Networks",
        "Knowledge Representation"
    ],
    "DevOps": [
        "Continuous Integration",
        "Continuous Deployment",
        "Infrastructure as Code",
        "Containerization",
        "Monitoring"
    ],
    "Cloud Computing": [
        "AWS",
        "Azure",
        "Google Cloud",
        "Serverless Computing",
        "Cloud Security"
    ]
}

def decompose_skill(skill_name):
    """
    Break down a skill into subskills using predefined hierarchy or semantic similarity
    
    Args:
        skill_name (str): The name of the skill to decompose
    
    Returns:
        dict: A JSON tree structure of skill and subskills
    """
    print(f"Decomposing skill: {skill_name}")
    if skill_name in SKILL_HIERARCHY:
        # Return predefined hierarchy if available
        print(f"Found skill {skill_name} in hierarchy")
        subskills = SKILL_HIERARCHY[skill_name]
        skill_tree = {
            "name": skill_name,
            "children": [{"name": subskill, "children": []} for subskill in subskills]
        }
        return skill_tree
    elif not ML_AVAILABLE:
        # Fallback for when ML is not available
        print(f"ML not available, using fallback for {skill_name}")
        # Return a generic skill breakdown
        generic_subskills = ["Fundamentals", "Intermediate Concepts", "Advanced Topics"]
        skill_tree = {
            "name": skill_name,
            "children": [{"name": f"{skill_name} {subskill}", "children": []} for subskill in generic_subskills]
        }
        return skill_tree
    else:
        # Use semantic similarity to find the most related skill
        skill_embedding = model.encode(skill_name)
        
        # Compute similarities with known skills
        known_skills = list(SKILL_HIERARCHY.keys())
        known_embeddings = model.encode(known_skills)
        
        # Find the most similar skill
        similarities = util.cos_sim(skill_embedding, known_embeddings)[0]
        best_match_idx = np.argmax(similarities)
        best_match = known_skills[best_match_idx]
        similarity_score = similarities[best_match_idx].item()
        
        # If similarity is high enough, use that skill's hierarchy
        if similarity_score > 0.7:
            subskills = SKILL_HIERARCHY[best_match]
            skill_tree = {
                "name": skill_name,
                "description": f"Similar to {best_match}",
                "children": [{"name": subskill, "children": []} for subskill in subskills]
            }
            return skill_tree
        else:
            # Default decomposition for unknown skills
            return {
                "name": skill_name,
                "children": [
                    {"name": f"Learning {skill_name} basics", "children": []},
                    {"name": f"Intermediate {skill_name}", "children": []},
                    {"name": f"Advanced {skill_name}", "children": []}
                ]
            }

def generate_learning_path(skill_name):
    """
    Generate a learning path for a given skill based on prerequisite relationships
    
    Args:
        skill_name (str): The name of the skill for which to generate a path
    
    Returns:
        list: An ordered list of skills and subskills to learn
    """
    print(f"Generating learning path for: {skill_name}")
    skill_tree = decompose_skill(skill_name)
    learning_path = []
    
    # Flatten the tree in a sensible learning order
    def traverse_tree(node, path):
        path.append(node["name"])
        for child in node["children"]:
            traverse_tree(child, path)
    
    traverse_tree(skill_tree, learning_path)
    print(f"Learning path: {learning_path}")
    return learning_path

def get_resources_for_skill(skill_name):
    """
    Get high-quality curated resources for a skill using enhanced search
    
    Args:
        skill_name (str): The name of the skill
        
    Returns:
        list: List of high-quality resource objects
    """
    print(f"Getting high-quality resources for skill: {skill_name}")
    
    # Try to get resources using the enhanced search system
    try:
        # Import the enhanced resource search utility
        from backend.utils.resource_search import get_resources_for_skill as search_resources
        from backend.utils.curated_resources import get_curated_resources
        
        # First try curated resources
        curated = get_curated_resources(skill_name)
        if curated:
            print(f"Found {len(curated)} curated resources for {skill_name}")
            return curated
        
        # Search for high-quality resources with the enhanced utility
        resources = search_resources(skill_name, max_per_type=2)
        
        # If we got resources, return them
        if resources and len(resources) > 0:
            print(f"Found {len(resources)} high-quality resources for {skill_name}")
            # Sort by quality score
            resources.sort(key=lambda x: x.get('quality_score', 0), reverse=True)
            return resources
    except Exception as e:
        print(f"Error getting dynamic resources: {str(e)}")
    
    # Enhanced fallback resources with better quality
    print(f"Using enhanced fallback resources for {skill_name}")
    
    # Create more targeted fallback resources based on common skill patterns
    skill_lower = skill_name.lower()
    
    if any(term in skill_lower for term in ['python', 'programming']):
        fallback_resources = [
            {
                "title": "Python Official Tutorial",
                "url": "https://docs.python.org/3/tutorial/",
                "resource_type": "documentation",
                "description": "Official Python tutorial from python.org",
                "quality_score": 95
            },
            {
                "title": f"{skill_name} on freeCodeCamp",
                "url": f"https://www.freecodecamp.org/learn/",
                "resource_type": "course",
                "description": f"Free interactive {skill_name} course",
                "quality_score": 88
            }
        ]
    elif any(term in skill_lower for term in ['web', 'html', 'css', 'javascript']):
        fallback_resources = [
            {
                "title": "MDN Web Docs",
                "url": "https://developer.mozilla.org/en-US/",
                "resource_type": "documentation",
                "description": f"Mozilla Developer Network guide for {skill_name}",
                "quality_score": 95
            },
            {
                "title": f"{skill_name} Tutorial on W3Schools",
                "url": "https://www.w3schools.com/",
                "resource_type": "article",
                "description": f"Comprehensive {skill_name} tutorial with examples",
                "quality_score": 82
            }
        ]
    else:
        # Generic high-quality fallback
        fallback_resources = [
            {
                "title": f"Learn {skill_name} - Coursera",
                "url": f"https://www.coursera.org/search?query={skill_name.replace(' ', '%20')}",
                "resource_type": "course",
                "description": f"University-level courses on {skill_name}",
                "quality_score": 85
            },
            {
                "title": f"{skill_name} Tutorial - freeCodeCamp",
                "url": "https://www.freecodecamp.org/learn/",
                "resource_type": "course",
                "description": f"Free comprehensive {skill_name} curriculum",
                "quality_score": 88
            }
        ]
        fallback_resources += [
        {
            "title": f"Official {skill_name} Documentation",
            "url": f"https://www.google.com/search?q={skill_name.replace(' ', '+')}+documentation",
            "resource_type": "documentation",
            "description": f"Official documentation for {skill_name}"
        },
        {
            "title": f"{skill_name} GitHub Projects",
            "url": f"https://github.com/search?q={skill_name.replace(' ', '+')}",
            "resource_type": "github",
            "description": f"Popular GitHub projects related to {skill_name}"
        }
    ]
    
    # Predefined resources for common skills
    resource_map = {
        "Python Basics": [
            {
                "title": "Python Official Documentation",
                "url": "https://docs.python.org/3/tutorial/",
                "resource_type": "documentation",
                "description": "The official Python tutorial"
            },
            {
                "title": "Learn Python in 10 Minutes",
                "url": "https://www.youtube.com/watch?v=_uQrJ0TkZlc",
                "resource_type": "video",
                "description": "Quick Python crash course"
            }
        ],
        "Data Science": [
            {
                "title": "Data Science Roadmap",
                "url": "https://github.com/khuyentran1401/Data-science-roadmap",
                "resource_type": "github",
                "description": "A comprehensive roadmap for data science"
            }
        ]
    }
    
    return resource_map.get(skill_name, generic_resources) + fallback_resources
