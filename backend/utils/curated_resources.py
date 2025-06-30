"""
Curated High-Quality Resources for SkillSprint
=============================================
This module contains manually vetted, high-quality learning resources
for various skills and their subskills, ensuring users get the best 
free educational content tailored to each specific topic.
"""

from datetime import datetime
import re

# Comprehensive subskill-specific resources for detailed learning paths
SUBSKILL_RESOURCES = {
    # Data Structures & Algorithms Subskills
    "arrays": [
        {
            "title": "Array Data Structure - GeeksforGeeks",
            "url": "https://www.geeksforgeeks.org/array-data-structure/",
            "description": "Comprehensive guide to arrays with problems and solutions",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Array Problems - LeetCode",
            "url": "https://leetcode.com/tag/array/",
            "description": "Practice array problems with detailed solutions",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "Arrays Visualization",
            "url": "https://www.cs.usfca.edu/~galles/visualization/Array.html",
            "description": "Interactive array operations visualization",
            "resource_type": "article",
            "quality_score": 88
        }
    ],
    "linked lists": [
        {
            "title": "Linked List Data Structure",
            "url": "https://www.geeksforgeeks.org/data-structures/linked-list/",
            "description": "Complete guide to linked lists with implementations",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Linked List Visualization",
            "url": "https://www.cs.usfca.edu/~galles/visualization/LinkedList.html",
            "description": "Interactive linked list operations",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "Linked List Problems - HackerRank",
            "url": "https://www.hackerrank.com/domains/data-structures/linked-lists",
            "description": "Practice linked list problems with step-by-step solutions",
            "resource_type": "course",
            "quality_score": 88
        }
    ],
    "stacks": [
        {
            "title": "Stack Data Structure",
            "url": "https://www.geeksforgeeks.org/stack-data-structure/",
            "description": "Complete stack implementation and applications",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Stack Visualization",
            "url": "https://www.cs.usfca.edu/~galles/visualization/StackArray.html",
            "description": "Interactive stack operations visualization",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "Stack Applications Tutorial",
            "url": "https://www.programiz.com/dsa/stack",
            "description": "Stack applications with real-world examples",
            "resource_type": "course",
            "quality_score": 88
        }
    ],
    "queues": [
        {
            "title": "Queue Data Structure",
            "url": "https://www.geeksforgeeks.org/queue-data-structure/",
            "description": "Comprehensive queue implementation guide",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Queue Visualization",
            "url": "https://www.cs.usfca.edu/~galles/visualization/QueueArray.html",
            "description": "Interactive queue operations",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "Priority Queue Tutorial",
            "url": "https://www.programiz.com/dsa/priority-queue",
            "description": "Priority queues and heap implementation",
            "resource_type": "course",
            "quality_score": 88
        }
    ],
    "trees": [
        {
            "title": "Tree Data Structure",
            "url": "https://www.geeksforgeeks.org/binary-tree-data-structure/",
            "description": "Complete guide to tree data structures",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Binary Tree Visualization",
            "url": "https://www.cs.usfca.edu/~galles/visualization/BST.html",
            "description": "Interactive binary tree operations",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "Tree Traversal Algorithms",
            "url": "https://www.programiz.com/dsa/tree-traversal",
            "description": "In-depth tree traversal techniques",
            "resource_type": "course",
            "quality_score": 88
        }
    ],
    "binary trees": [
        {
            "title": "Binary Tree Complete Guide",
            "url": "https://www.geeksforgeeks.org/binary-tree-data-structure/",
            "description": "Comprehensive binary tree tutorial with problems",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Binary Tree Problems - LeetCode",
            "url": "https://leetcode.com/tag/binary-tree/",
            "description": "Practice binary tree problems",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "Binary Tree Visualization",
            "url": "https://www.cs.usfca.edu/~galles/visualization/BST.html",
            "description": "Interactive binary tree operations",
            "resource_type": "article",
            "quality_score": 88
        }
    ],
    "graphs": [
        {
            "title": "Graph Data Structure",
            "url": "https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/",
            "description": "Complete graph algorithms and implementations",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Graph Visualization",
            "url": "https://www.cs.usfca.edu/~galles/visualization/BFS.html",
            "description": "Interactive graph traversal algorithms",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "Graph Algorithms Course",
            "url": "https://www.coursera.org/learn/algorithms-on-graphs",
            "description": "Free algorithms on graphs course",
            "resource_type": "course",
            "quality_score": 88
        }
    ],
    "sorting algorithms": [
        {
            "title": "Sorting Algorithms Guide",
            "url": "https://www.geeksforgeeks.org/sorting-algorithms/",
            "description": "Complete guide to all sorting algorithms",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Sorting Visualization",
            "url": "https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html",
            "description": "Interactive sorting algorithm visualization",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "Sorting Algorithms Comparison",
            "url": "https://www.programiz.com/dsa/sorting-algorithm",
            "description": "Time complexity analysis of sorting algorithms",
            "resource_type": "course",
            "quality_score": 88
        }
    ],
    "searching algorithms": [
        {
            "title": "Searching Algorithms",
            "url": "https://www.geeksforgeeks.org/searching-algorithms/",
            "description": "Binary search, linear search, and advanced techniques",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Search Visualization",
            "url": "https://www.cs.usfca.edu/~galles/visualization/Search.html",
            "description": "Interactive searching algorithm visualization",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "Binary Search Mastery",
            "url": "https://leetcode.com/explore/learn/card/binary-search/",
            "description": "Complete binary search tutorial with problems",
            "resource_type": "course",
            "quality_score": 88
        }
    ],
    "dynamic programming": [
        {
            "title": "Dynamic Programming Guide",
            "url": "https://www.geeksforgeeks.org/dynamic-programming/",
            "description": "Complete dynamic programming tutorial with patterns",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "DP Patterns for Coding Interviews",
            "url": "https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns",
            "description": "Essential DP patterns with examples",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "Dynamic Programming Course",
            "url": "https://www.coursera.org/learn/algorithmic-toolbox",
            "description": "Free algorithmic toolbox course covering DP",
            "resource_type": "course",
            "quality_score": 88
        }
    ],
    "recursion": [
        {
            "title": "Recursion Complete Guide",
            "url": "https://www.geeksforgeeks.org/recursion/",
            "description": "Master recursion with examples and practice problems",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Recursion Visualization",
            "url": "https://www.cs.usfca.edu/~galles/visualization/RecursiveFactorial.html",
            "description": "Interactive recursion visualization",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "Thinking Recursively",
            "url": "https://think-recursively.com/",
            "description": "Learn to think recursively with interactive examples",
            "resource_type": "course",
            "quality_score": 88
        }
    ],

    # Web Development Subskills
    "html basics": [
        {
            "title": "HTML5 Tutorial - MDN",
            "url": "https://developer.mozilla.org/en-US/docs/Learn/HTML",
            "description": "Complete HTML5 tutorial from Mozilla",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "HTML Tutorial - W3Schools",
            "url": "https://www.w3schools.com/html/",
            "description": "Interactive HTML tutorial with examples",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "HTML Semantic Elements",
            "url": "https://www.freecodecamp.org/news/semantic-html5-elements/",
            "description": "Learn semantic HTML for better accessibility",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "css styling": [
        {
            "title": "CSS Complete Guide - MDN",
            "url": "https://developer.mozilla.org/en-US/docs/Learn/CSS",
            "description": "Comprehensive CSS learning guide",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "CSS Grid Garden",
            "url": "https://cssgridgarden.com/",
            "description": "Learn CSS Grid through interactive games",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "Flexbox Froggy",
            "url": "https://flexboxfroggy.com/",
            "description": "Master CSS Flexbox with fun exercises",
            "resource_type": "course",
            "quality_score": 90
        }
    ],
    "javascript fundamentals": [
        {
            "title": "JavaScript.info - Modern Tutorial",
            "url": "https://javascript.info/",
            "description": "The modern JavaScript tutorial covering all fundamentals",
            "resource_type": "article",
            "quality_score": 95
        },
        {
            "title": "You Don't Know JS - Kyle Simpson",
            "url": "https://github.com/getify/You-Dont-Know-JS",
            "description": "Deep dive into JavaScript fundamentals",
            "resource_type": "github",
            "quality_score": 92
        },
        {
            "title": "JavaScript30",
            "url": "https://javascript30.com/",
            "description": "30 projects in 30 days with vanilla JavaScript",
            "resource_type": "course",
            "quality_score": 88
        }
    ],
    "dom manipulation": [
        {
            "title": "DOM Manipulation Guide",
            "url": "https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction",
            "description": "Complete DOM manipulation tutorial",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "DOM Manipulation Crash Course",
            "url": "https://www.freecodecamp.org/news/dom-manipulation-htmlcollection-vs-nodelist/",
            "description": "Practical DOM manipulation techniques",
            "resource_type": "article",
            "quality_score": 88
        },
        {
            "title": "Interactive DOM Tutorial",
            "url": "https://www.w3schools.com/js/js_htmldom.asp",
            "description": "Hands-on DOM manipulation examples",
            "resource_type": "course",
            "quality_score": 85
        }
    ],

    # Machine Learning Subskills
    "linear algebra": [
        {
            "title": "Linear Algebra - Khan Academy",
            "url": "https://www.khanacademy.org/math/linear-algebra",
            "description": "Complete linear algebra course with interactive exercises",
            "resource_type": "course",
            "quality_score": 95
        },
        {
            "title": "3Blue1Brown - Essence of Linear Algebra",
            "url": "https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab",
            "description": "Visual and intuitive approach to linear algebra",
            "resource_type": "video",
            "quality_score": 98
        },
        {
            "title": "Linear Algebra for ML",
            "url": "https://machinelearningmastery.com/linear-algebra-machine-learning/",
            "description": "Linear algebra concepts essential for machine learning",
            "resource_type": "article",
            "quality_score": 88
        }
    ],
    "statistics": [
        {
            "title": "Statistics - Khan Academy",
            "url": "https://www.khanacademy.org/math/statistics-probability",
            "description": "Comprehensive statistics and probability course",
            "resource_type": "course",
            "quality_score": 95
        },
        {
            "title": "Think Stats",
            "url": "https://greenteapress.com/thinkstats2/",
            "description": "Free statistics textbook with Python examples",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "Statistical Learning - Stanford",
            "url": "https://online.stanford.edu/courses/sohs-ystatslearning-statistical-learning",
            "description": "Free statistical learning course from Stanford",
            "resource_type": "course",
            "quality_score": 92
        }
    ],
    "supervised learning": [
        {
            "title": "Supervised Learning Guide",
            "url": "https://scikit-learn.org/stable/supervised_learning.html",
            "description": "Scikit-learn's comprehensive supervised learning guide",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Machine Learning Course - Andrew Ng",
            "url": "https://www.coursera.org/learn/machine-learning",
            "description": "Famous ML course covering supervised learning",
            "resource_type": "course",
            "quality_score": 98
        },
        {
            "title": "Supervised Learning Algorithms",
            "url": "https://machinelearningmastery.com/supervised-and-unsupervised-machine-learning-algorithms/",
            "description": "Overview of key supervised learning algorithms",
            "resource_type": "article",
            "quality_score": 88
        }
    ],

    # Python Subskills
    "python basics": [
        {
            "title": "Python.org Official Tutorial",
            "url": "https://docs.python.org/3/tutorial/",
            "description": "The official Python tutorial - start here",
            "resource_type": "documentation",
            "quality_score": 98
        },
        {
            "title": "Automate the Boring Stuff",
            "url": "https://automatetheboringstuff.com/",
            "description": "Learn Python through practical automation projects",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Python for Everybody",
            "url": "https://www.py4e.com/",
            "description": "Free Python course from University of Michigan",
            "resource_type": "course",
            "quality_score": 90
        }
    ],
    "object oriented programming": [
        {
            "title": "OOP in Python - Real Python",
            "url": "https://realpython.com/python3-object-oriented-programming/",
            "description": "Comprehensive guide to OOP concepts in Python",
            "resource_type": "article",
            "quality_score": 95
        },
        {
            "title": "Python OOP Tutorial",
            "url": "https://www.programiz.com/python-programming/object-oriented-programming",
            "description": "Step-by-step OOP tutorial with examples",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "OOP Design Patterns",
            "url": "https://github.com/faif/python-patterns",
            "description": "Python implementation of design patterns",
            "resource_type": "github",
            "quality_score": 85
        }
    ],
    "data structures in python": [
        {
            "title": "Python Data Structures",
            "url": "https://docs.python.org/3/tutorial/datastructures.html",
            "description": "Official Python data structures documentation",
            "resource_type": "documentation",
            "quality_score": 98
        },
        {
            "title": "Python Collections Module",
            "url": "https://realpython.com/python-collections-module/",
            "description": "Advanced data structures using collections",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "Data Structures and Algorithms in Python",
            "url": "https://github.com/TheAlgorithms/Python",
            "description": "Python implementations of data structures and algorithms",
            "resource_type": "github",
            "quality_score": 88
        }
    ]
}

# Manually curated high-quality resources for common skills
CURATED_RESOURCES = {
    "python": [
        {
            "title": "Python Official Tutorial",
            "url": "https://docs.python.org/3/tutorial/",
            "description": "The official Python tutorial from python.org - comprehensive and authoritative",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Python for Everybody (Free Course)",
            "url": "https://www.py4e.com/",
            "description": "Free comprehensive Python course taught by Dr. Chuck Severance - completely free to audit",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "Automate the Boring Stuff with Python",
            "url": "https://automatetheboringstuff.com/",
            "description": "Free online book teaching practical Python programming for total beginners",
            "resource_type": "article",
            "quality_score": 88
        },
        {
            "title": "Python Crash Course - Eric Matthes",
            "url": "https://github.com/ehmatthes/pcc_2e",
            "description": "Code examples and exercises from the popular Python Crash Course book",
            "resource_type": "github",
            "quality_score": 85
        }
    ],
    "javascript": [
        {
            "title": "MDN JavaScript Guide",
            "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide",
            "description": "Mozilla Developer Network's comprehensive JavaScript guide - the gold standard",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "JavaScript.info - The Modern JavaScript Tutorial",
            "url": "https://javascript.info/",
            "description": "Comprehensive, well-structured JavaScript tutorial covering modern standards",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "freeCodeCamp JavaScript Algorithms and Data Structures",
            "url": "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/",
            "description": "Free interactive JavaScript course with projects and certification",
            "resource_type": "course",
            "quality_score": 88
        }
    ],
    "react": [
        {
            "title": "React Official Documentation",
            "url": "https://reactjs.org/docs/getting-started.html",
            "description": "Official React documentation with tutorials and guides",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "React Tutorial for Beginners - Programming with Mosh",
            "url": "https://www.youtube.com/watch?v=Ke90Tje7VS0",
            "description": "Comprehensive React tutorial covering all fundamentals",
            "resource_type": "video",
            "quality_score": 90
        },
        {
            "title": "React Developer Roadmap",
            "url": "https://github.com/adam-golab/react-developer-roadmap",
            "description": "Complete roadmap for becoming a React developer with resources",
            "resource_type": "github",
            "quality_score": 87
        }
    ],
    "data science": [
        {
            "title": "Python Data Science Handbook",
            "url": "https://jakevdp.github.io/PythonDataScienceHandbook/",
            "description": "Free online book covering essential tools for working with data in Python",
            "resource_type": "article",
            "quality_score": 93
        },
        {
            "title": "Coursera Data Science Specialization",
            "url": "https://www.coursera.org/specializations/jhu-data-science",
            "description": "Johns Hopkins University's comprehensive data science specialization",
            "resource_type": "course",
            "quality_score": 91
        },
        {
            "title": "Kaggle Learn",
            "url": "https://www.kaggle.com/learn",
            "description": "Free micro-courses on data science topics with hands-on practice",
            "resource_type": "course",
            "quality_score": 89
        }
    ],
    "machine learning": [
        {
            "title": "Machine Learning Course - Andrew Ng",
            "url": "https://www.coursera.org/learn/machine-learning",
            "description": "Stanford's famous machine learning course taught by Andrew Ng",
            "resource_type": "course",
            "quality_score": 95
        },
        {
            "title": "Scikit-learn User Guide",
            "url": "https://scikit-learn.org/stable/user_guide.html",
            "description": "Comprehensive guide to machine learning with Python's scikit-learn",
            "resource_type": "documentation",
            "quality_score": 90
        },
        {
            "title": "Machine Learning Yearning - Andrew Ng",
            "url": "https://github.com/ajaymache/machine-learning-yearning",
            "description": "Free book on machine learning project strategy by Andrew Ng",
            "resource_type": "github",
            "quality_score": 88
        }
    ],
    "web development": [
        {
            "title": "freeCodeCamp Web Development Curriculum",
            "url": "https://www.freecodecamp.org/learn/",
            "description": "Complete free web development curriculum with projects and certifications",
            "resource_type": "course",
            "quality_score": 92
        },
        {
            "title": "MDN Web Docs",
            "url": "https://developer.mozilla.org/en-US/docs/Learn",
            "description": "Mozilla's comprehensive web development learning area",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "The Odin Project",
            "url": "https://www.theodinproject.com/",
            "description": "Free full stack curriculum with project-based learning",
            "resource_type": "course",
            "quality_score": 90
        }
    ],
    "html": [
        {
            "title": "MDN HTML Basics",
            "url": "https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics",
            "description": "Mozilla's definitive guide to HTML fundamentals",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "HTML Tutorial - W3Schools",
            "url": "https://www.w3schools.com/html/",
            "description": "Comprehensive HTML tutorial with examples and exercises",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "css": [
        {
            "title": "MDN CSS Basics",
            "url": "https://developer.mozilla.org/en-US/docs/Learn/CSS",
            "description": "Mozilla's comprehensive CSS learning guide",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "CSS-Tricks",
            "url": "https://css-tricks.com/",
            "description": "Popular website with CSS tutorials, guides, and reference materials",
            "resource_type": "article",
            "quality_score": 88
        },
        {
            "title": "Flexbox Froggy",
            "url": "https://flexboxfroggy.com/",
            "description": "Interactive game for learning CSS Flexbox",
            "resource_type": "course",
            "quality_score": 85
        }
    ],
    "data structures": [
        {
            "title": "Striver's A2Z DSA Course/Sheet",
            "url": "https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/",
            "description": "Comprehensive step-by-step DSA sheet by Striver - most popular DSA preparation resource",
            "resource_type": "course",
            "quality_score": 98
        },
        {
            "title": "Data Structures Visualizations",
            "url": "https://www.cs.usfca.edu/~galles/visualization/Algorithms.html",
            "description": "Interactive data structure and algorithm visualizations",
            "resource_type": "article",
            "quality_score": 95
        },
        {
            "title": "GeeksforGeeks Data Structures",
            "url": "https://www.geeksforgeeks.org/data-structures/",
            "description": "Comprehensive data structures tutorials",
            "resource_type": "article",
            "quality_score": 88
        }
    ],
    "algorithms": [
        {
            "title": "Striver's A2Z DSA Course/Sheet",
            "url": "https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/",
            "description": "Comprehensive step-by-step DSA sheet by Striver - most popular DSA preparation resource",
            "resource_type": "course",
            "quality_score": 98
        },
        {
            "title": "Introduction to Algorithms - MIT",
            "url": "https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/",
            "description": "Free MIT algorithms course with video lectures",
            "resource_type": "course",
            "quality_score": 95
        },
        {
            "title": "Algorithm Visualizer",
            "url": "https://algorithm-visualizer.org/",
            "description": "Interactive algorithm visualizations",
            "resource_type": "article",
            "quality_score": 90
        }
    ]
}

def get_curated_resources(skill_name):
    """
    Get curated resources for a skill if available.
    
    Args:
        skill_name (str): The skill name to search for
        
    Returns:
        list: List of curated resource dictionaries, or empty list if none found
    """
    skill_lower = skill_name.lower().strip()
    
    # First check for exact subskill matches
    subskill_resources = get_subskill_resources(skill_name)
    if subskill_resources:
        return subskill_resources
    
    # Try exact match first in main skills
    if skill_lower in CURATED_RESOURCES:
        return CURATED_RESOURCES[skill_lower]
    
    # Try partial matches - check if skill name contains any of our curated skills
    for curated_skill, resources in CURATED_RESOURCES.items():
        if curated_skill in skill_lower or skill_lower in curated_skill:
            return resources
    
    # Try keyword matching for common variations
    skill_keywords = {
        "python": ["python", "py"],
        "javascript": ["javascript", "js", "ecmascript"],
        "react": ["react", "reactjs", "react.js"],
        "data science": ["data science", "data analysis", "analytics"],
        "machine learning": ["machine learning", "ml", "artificial intelligence", "ai"],
        "web development": ["web development", "web dev", "frontend", "backend"],
        "html": ["html", "html5", "markup"],
        "css": ["css", "css3", "styling", "styles"],
        "data structures": ["data structures", "data structure", "dsa", "ds"],
        "algorithms": ["algorithms", "algorithm", "dsa", "algo"]
    }
    
    for curated_skill, keywords in skill_keywords.items():
        for keyword in keywords:
            if keyword in skill_lower:
                return CURATED_RESOURCES.get(curated_skill, [])
    
    return []

def get_subskill_resources(skill_name):
    """
    Get specific resources for subskills to ensure unique, high-quality content.
    
    Args:
        skill_name (str): The subskill name to search for
        
    Returns:
        list: List of subskill-specific resource dictionaries, or empty list if none found
    """
    skill_lower = skill_name.lower().strip()
    
    # Direct exact match
    if skill_lower in SUBSKILL_RESOURCES:
        return SUBSKILL_RESOURCES[skill_lower]
    
    # Check for partial matches and variations
    subskill_variations = {
        "array": ["arrays", "array", "array problems", "array data structure"],
        "linked list": ["linked lists", "linked list", "linkedlist", "singly linked list", "doubly linked list"],
        "stack": ["stacks", "stack", "stack data structure", "lifo"],
        "queue": ["queues", "queue", "queue data structure", "fifo", "priority queue"],
        "tree": ["trees", "tree", "binary tree", "tree data structure", "binary search tree", "bst"],
        "binary tree": ["binary trees", "binary tree", "bt", "tree traversal"],
        "graph": ["graphs", "graph", "graph algorithms", "graph theory", "directed graph", "undirected graph"],
        "sorting": ["sorting algorithms", "sorting", "sort", "bubble sort", "merge sort", "quick sort", "heap sort"],
        "searching": ["searching algorithms", "searching", "search", "binary search", "linear search"],
        "dynamic programming": ["dynamic programming", "dp", "memoization", "tabulation"],
        "recursion": ["recursion", "recursive", "recursive algorithms"],
        "greedy": ["greedy algorithms", "greedy", "greedy approach"],
        "backtracking": ["backtracking", "backtrack", "backtracking algorithms"],
        
        # Web Development subskills
        "html": ["html basics", "html", "html5", "markup", "semantic html"],
        "css": ["css styling", "css", "css3", "styling", "styles", "flexbox", "grid"],
        "javascript": ["javascript fundamentals", "javascript", "js", "vanilla javascript"],
        "dom": ["dom manipulation", "dom", "document object model"],
        
        # Machine Learning subskills
        "linear algebra": ["linear algebra", "matrices", "vectors", "eigenvalues"],
        "statistics": ["statistics", "probability", "statistical analysis"],
        "supervised learning": ["supervised learning", "classification", "regression"],
        "unsupervised learning": ["unsupervised learning", "clustering", "dimensionality reduction"],
        
        # Python subskills
        "python basics": ["python basics", "python fundamentals", "python syntax"],
        "oop": ["object oriented programming", "oop", "classes", "objects", "inheritance"],
        "data structures python": ["data structures in python", "python data structures", "lists", "dictionaries", "tuples"]
    }
    
    # Find matching subskill
    for canonical_skill, variations in subskill_variations.items():
        for variation in variations:
            if variation in skill_lower or skill_lower in variation:
                # Look up the canonical skill in SUBSKILL_RESOURCES
                if canonical_skill in SUBSKILL_RESOURCES:
                    return SUBSKILL_RESOURCES[canonical_skill]
                # Also check variations directly
                elif variation in SUBSKILL_RESOURCES:
                    return SUBSKILL_RESOURCES[variation]
    
    return []

def calculate_resource_quality(title, description, url, view_count=0, likes=0, domain_bonus=True):
    """
    Calculate a quality score for a resource based on various signals.
    
    Args:
        title (str): Resource title
        description (str): Resource description
        url (str): Resource URL
        view_count (int): Number of views (if available)
        likes (int): Number of likes (if available)
        domain_bonus (bool): Whether to apply domain authority bonus
        
    Returns:
        int: Quality score (0-100)
    """
    score = 0
    title_lower = title.lower()
    desc_lower = description.lower() if description else ""
    
    # Base score for educational content
    educational_terms = [
        "tutorial", "course", "guide", "learn", "introduction", "beginner",
        "fundamentals", "basics", "getting started", "step by step",
        "comprehensive", "complete", "masterclass", "bootcamp"
    ]
    
    for term in educational_terms:
        if term in title_lower or term in desc_lower:
            score += 8
            break  # Only give bonus once
    
    # Bonus for comprehensive/complete content
    comprehensive_terms = ["complete", "comprehensive", "full", "entire", "ultimate"]
    for term in comprehensive_terms:
        if term in title_lower:
            score += 10
            break
    
    # Bonus for structured learning
    structured_terms = ["roadmap", "path", "curriculum", "syllabus", "structured"]
    for term in structured_terms:
        if term in title_lower or term in desc_lower:
            score += 8
            break
    
    # Domain authority bonus
    if domain_bonus:
        authoritative_domains = [
            "docs.python.org", "developer.mozilla.org", "reactjs.org",
            "freecodecamp.org", "coursera.org", "edx.org", "udacity.com",
            "khanacademy.org", "w3schools.com", "css-tricks.com",
            "github.io", "kaggle.com", "scikit-learn.org",
            "tensorflow.org", "pytorch.org", "javascript.info"
        ]
        
        for domain in authoritative_domains:
            if domain in url:
                score += 25
                break
        
        # Additional bonus for official documentation
        official_terms = ["official", "docs", "documentation"]
        for term in official_terms:
            if term in url or term in title_lower:
                score += 15
                break
    
    # Engagement metrics (capped to prevent skewing)
    if view_count > 0:
        score += min(view_count / 10000, 15)  # Cap at 15 points
    
    if likes > 0:
        score += min(likes / 1000, 10)  # Cap at 10 points
    
    # Freshness check (bonus for recent content)
    score += check_resource_freshness(url)
    
    # Penalty for clickbait indicators
    clickbait_terms = ["you won't believe", "amazing", "incredible", "shocking"]
    for term in clickbait_terms:
        if term in title_lower:
            score -= 10
            break
    
    return max(0, min(100, score))  # Ensure score is between 0-100

def check_resource_freshness(url):
    """
    Check if a resource appears to be fresh/recent based on URL patterns.
    
    Args:
        url (str): The resource URL
        
    Returns:
        int: Freshness bonus points (0-15)
    """
    current_year = datetime.now().year
    
    # Look for year patterns in URL
    year_pattern = r'/20[1-9][0-9]/'
    matches = re.findall(year_pattern, url)
    
    if matches:
        years = [int(match.strip('/')) for match in matches]
        most_recent_year = max(years)
        
        # Bonus based on how recent the content appears to be
        years_old = current_year - most_recent_year
        if years_old <= 1:
            return 15  # Very recent
        elif years_old <= 2:
            return 10  # Recent
        elif years_old <= 3:
            return 5   # Moderately recent
    
    return 0  # No freshness bonus
