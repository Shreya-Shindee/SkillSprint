"""
Enhanced Resource Search for SkillSprint
=========================================
This module provides advanced resource search functionality with:
- Prioritized source ranking (official docs > GitHub > FreeCodeCamp > others)
- Quality scoring based on multiple factors
- Comprehensive resource type coverage
- Learning path generation with quizzes
"""

import asyncio
import aiohttp
import logging
from typing import List, Dict, Optional
from urllib.parse import quote_plus
import re
from datetime import datetime

from .curated_resources import get_curated_resources, calculate_resource_quality
from .resource_search import get_resources_for_skill as basic_search

logger = logging.getLogger(__name__)

# Priority ranking for different domains (higher = better)
DOMAIN_PRIORITIES = {
    # Official documentation gets highest priority
    'docs.python.org': 100,
    'developer.mozilla.org': 100,
    'reactjs.org': 100,
    'nodejs.org': 100,
    'docs.microsoft.com': 95,
    
    # Educational platforms
    'freecodecamp.org': 90,
    'codecademy.com': 85,
    'khanacademy.org': 85,
    'coursera.org': 80,
    'edx.org': 80,
    'udacity.com': 75,
    
    # GitHub repositories
    'github.com': 85,
    
    # Quality tutorial sites
    'tutorialspoint.com': 70,
    'w3schools.com': 65,
    'geeksforgeeks.org': 70,
    'real-python.com': 85,
    'javascript.info': 90,
    
    # Video platforms
    'youtube.com': 60,  # Variable quality
    'vimeo.com': 55,
    
    # Other
    'medium.com': 50,
    'dev.to': 55,
    'stackoverflow.com': 75,
}

async def enhanced_resource_search(skill_name: str, max_results: int = 10) -> List[Dict]:
    """
    Enhanced resource search with prioritized sources and quality scoring.
    
    Args:
        skill_name: The skill to search for
        max_results: Maximum number of resources to return
        
    Returns:
        List of high-quality resource dictionaries sorted by priority
    """
    logger.info(f"Starting enhanced search for: {skill_name}")
    
    all_resources = []
    
    # Step 1: Get curated resources first (highest quality)
    curated = get_curated_resources(skill_name)
    if curated:
        logger.info(f"Found {len(curated)} curated resources")
        all_resources.extend(curated)
    
    # Step 2: Search official documentation
    official_docs = await search_official_documentation(skill_name)
    all_resources.extend(official_docs)
    
    # Step 3: Search GitHub for relevant repositories
    github_repos = await search_github_repositories(skill_name)
    all_resources.extend(github_repos)
    
    # Step 4: Search educational platforms
    educational_resources = await search_educational_platforms(skill_name)
    all_resources.extend(educational_resources)
    
    # Step 5: Search for video tutorials
    video_resources = await search_video_tutorials(skill_name)
    all_resources.extend(video_resources)
    
    # Step 6: Remove duplicates and score
    unique_resources = remove_duplicates(all_resources)
    scored_resources = [score_resource(r) for r in unique_resources]
    
    # Sort by score and return top results
    scored_resources.sort(key=lambda x: x['quality_score'], reverse=True)
    
    logger.info(f"Enhanced search completed. Found {len(scored_resources)} unique resources")
    return scored_resources[:max_results]

async def search_official_documentation(skill_name: str) -> List[Dict]:
    """Search for official documentation"""
    docs_map = {
        'python': 'https://docs.python.org/3/',
        'javascript': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript',
        'react': 'https://reactjs.org/docs/',
        'node.js': 'https://nodejs.org/en/docs/',
        'typescript': 'https://www.typescriptlang.org/docs/',
        'django': 'https://docs.djangoproject.com/',
        'flask': 'https://flask.palletsprojects.com/',
        'vue': 'https://vuejs.org/guide/',
        'angular': 'https://angular.io/docs',
        'css': 'https://developer.mozilla.org/en-US/docs/Web/CSS',
        'html': 'https://developer.mozilla.org/en-US/docs/Web/HTML',
    }
    
    resources = []
    skill_lower = skill_name.lower()
    
    for skill_key, url in docs_map.items():
        if skill_key in skill_lower or skill_lower in skill_key:
            resources.append({
                'title': f'Official {skill_name} Documentation',
                'url': url,
                'description': f'Official documentation for {skill_name}',
                'resource_type': 'documentation',
                'quality_score': 100,
                'priority_source': True
            })
    
    return resources

async def search_github_repositories(skill_name: str, max_results: int = 3) -> List[Dict]:
    """Search GitHub for high-quality repositories"""
    
    # Known high-quality repository patterns
    quality_repos = {
        'python': [
            'https://github.com/TheAlgorithms/Python',
            'https://github.com/vinta/awesome-python',
            'https://github.com/jakevdp/PythonDataScienceHandbook'
        ],
        'javascript': [
            'https://github.com/airbnb/javascript',
            'https://github.com/getify/You-Dont-Know-JS',
            'https://github.com/leonardomso/33-js-concepts'
        ],
        'react': [
            'https://github.com/facebook/react',
            'https://github.com/enaqx/awesome-react',
            'https://github.com/adam-golab/react-developer-roadmap'
        ],
        'machine learning': [
            'https://github.com/microsoft/ML-For-Beginners',
            'https://github.com/ageron/handson-ml2',
            'https://github.com/josephmisiti/awesome-machine-learning'
        ],
        'data science': [
            'https://github.com/academic/awesome-datascience',
            'https://github.com/donnemartin/data-science-ipython-notebooks',
            'https://github.com/krzjoa/awesome-python-data-science'
        ]
    }
    
    resources = []
    skill_lower = skill_name.lower()
    
    for skill_key, repos in quality_repos.items():
        if skill_key in skill_lower or any(word in skill_lower for word in skill_key.split()):
            for repo_url in repos[:max_results]:
                repo_name = repo_url.split('/')[-1]
                resources.append({
                    'title': repo_name.replace('-', ' ').title(),
                    'url': repo_url,
                    'description': f'High-quality GitHub repository for {skill_name}',
                    'resource_type': 'github',
                    'quality_score': 85,
                    'priority_source': True
                })
    
    return resources

async def search_educational_platforms(skill_name: str) -> List[Dict]:
    """Search educational platforms for courses"""
    
    # FreeCodeCamp curriculum mapping
    fcc_curricula = {
        'javascript': 'https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/',
        'python': 'https://www.freecodecamp.org/learn/scientific-computing-with-python/',
        'data analysis': 'https://www.freecodecamp.org/learn/data-analysis-with-python/',
        'machine learning': 'https://www.freecodecamp.org/learn/machine-learning-with-python/',
        'web development': 'https://www.freecodecamp.org/learn/responsive-web-design/',
        'react': 'https://www.freecodecamp.org/learn/front-end-development-libraries/',
        'node.js': 'https://www.freecodecamp.org/learn/back-end-development-and-apis/',
    }
    
    resources = []
    skill_lower = skill_name.lower()
    
    for curriculum_key, url in fcc_curricula.items():
        if curriculum_key in skill_lower or any(word in skill_lower for word in curriculum_key.split()):
            resources.append({
                'title': f'FreeCodeCamp {skill_name} Certification',
                'url': url,
                'description': f'Free interactive {skill_name} course with projects and certification',
                'resource_type': 'course',
                'quality_score': 90,
                'priority_source': True
            })
    
    return resources

async def search_video_tutorials(skill_name: str) -> List[Dict]:
    """Search for high-quality video tutorials"""
    
    # Known high-quality YouTube channels and specific videos
    quality_channels = {
        'python': [
            {
                'title': 'Python Full Course for Beginners - Programming with Mosh',
                'url': 'https://www.youtube.com/watch?v=_uQrJ0TkZlc',
                'description': 'Complete Python tutorial for beginners by Programming with Mosh'
            },
            {
                'title': 'Automate the Boring Stuff with Python - Al Sweigart',
                'url': 'https://www.youtube.com/watch?v=1F_OgqRuSdI',
                'description': 'Learn Python by automating real-world tasks'
            }
        ],
        'javascript': [
            {
                'title': 'JavaScript Crash Course - Traversy Media',
                'url': 'https://www.youtube.com/watch?v=hdI2bqOjy3c',
                'description': 'Complete JavaScript crash course for beginners'
            },
            {
                'title': 'JavaScript Tutorial for Beginners - Programming with Mosh',
                'url': 'https://www.youtube.com/watch?v=W6NZfCO5SIk',
                'description': 'Comprehensive JavaScript tutorial covering all fundamentals'
            }
        ],
        'react': [
            {
                'title': 'React Course - Beginner\'s Tutorial - freeCodeCamp',
                'url': 'https://www.youtube.com/watch?v=DLX62G4lc44',
                'description': 'Complete React tutorial for beginners by freeCodeCamp'
            },
            {
                'title': 'React Tutorial for Beginners - Programming with Mosh',
                'url': 'https://www.youtube.com/watch?v=Ke90Tje7VS0',
                'description': 'Comprehensive React tutorial covering all fundamentals'
            }
        ]
    }
    
    resources = []
    skill_lower = skill_name.lower()
    
    for skill_key, videos in quality_channels.items():
        if skill_key in skill_lower:
            for video in videos:
                video['resource_type'] = 'video'
                video['quality_score'] = 75
                video['priority_source'] = True
                resources.append(video)
    
    return resources

def remove_duplicates(resources: List[Dict]) -> List[Dict]:
    """Remove duplicate resources based on URL"""
    seen_urls = set()
    unique_resources = []
    
    for resource in resources:
        url = resource.get('url', '')
        if url not in seen_urls:
            seen_urls.add(url)
            unique_resources.append(resource)
    
    return unique_resources

def score_resource(resource: Dict) -> Dict:
    """Score a resource based on multiple quality factors"""
    url = resource.get('url', '')
    title = resource.get('title', '')
    description = resource.get('description', '')
    
    # Start with existing quality score or calculate one
    if 'quality_score' not in resource:
        resource['quality_score'] = calculate_resource_quality(title, description, url)
    
    # Boost score for priority sources
    if resource.get('priority_source'):
        resource['quality_score'] += 10
    
    # Boost score based on domain priority
    for domain, priority in DOMAIN_PRIORITIES.items():
        if domain in url:
            resource['quality_score'] = max(resource['quality_score'], priority)
            break
    
    # Boost score for resource type
    resource_type = resource.get('resource_type', '')
    type_boost = {
        'documentation': 15,
        'course': 10,
        'github': 8,
        'article': 5,
        'video': 3
    }
    resource['quality_score'] += type_boost.get(resource_type, 0)
    
    # Ensure score doesn't exceed 100
    resource['quality_score'] = min(resource['quality_score'], 100)
    
    return resource

def generate_learning_path(skill_name: str, resources: List[Dict]) -> Dict:
    """Generate a structured learning path with phases and quizzes"""
    
    # Define learning phases
    phases = [
        {
            'name': 'Foundation',
            'description': 'Learn the basics and core concepts',
            'duration': '1-2 weeks',
            'resources': [],
            'quiz_topics': [
                f'Basic {skill_name} syntax',
                f'Core {skill_name} concepts',
                f'{skill_name} fundamentals'
            ]
        },
        {
            'name': 'Intermediate',
            'description': 'Build practical skills and understanding',
            'duration': '2-3 weeks',
            'resources': [],
            'quiz_topics': [
                f'Intermediate {skill_name} features',
                f'{skill_name} best practices',
                f'Common {skill_name} patterns'
            ]
        },
        {
            'name': 'Advanced',
            'description': 'Master advanced topics and real-world applications',
            'duration': '3-4 weeks',
            'resources': [],
            'quiz_topics': [
                f'Advanced {skill_name} concepts',
                f'{skill_name} performance optimization',
                f'Real-world {skill_name} applications'
            ]
        },
        {
            'name': 'Projects',
            'description': 'Apply your skills to build real projects',
            'duration': '2-3 weeks',
            'resources': [],
            'quiz_topics': [
                f'{skill_name} project planning',
                f'Debugging {skill_name} applications',
                f'{skill_name} deployment and testing'
            ]
        }
    ]
    
    # Distribute resources across phases based on type and difficulty
    for resource in resources:
        resource_type = resource.get('resource_type', '')
        title = resource.get('title', '').lower()
        
        if any(word in title for word in ['beginner', 'introduction', 'basics', 'getting started']):
            phases[0]['resources'].append(resource)
        elif any(word in title for word in ['advanced', 'expert', 'mastery', 'deep dive']):
            phases[2]['resources'].append(resource)
        elif resource_type == 'github':
            phases[3]['resources'].append(resource)
        else:
            phases[1]['resources'].append(resource)
    
    # Generate quiz questions for each phase
    for phase in phases:
        phase['quiz'] = generate_quiz_questions(skill_name, phase['quiz_topics'])
    
    return {
        'skill': skill_name,
        'total_duration': '8-12 weeks',
        'phases': phases,
        'total_resources': len(resources)
    }

def generate_quiz_questions(skill_name: str, topics: List[str]) -> List[Dict]:
    """Generate quiz questions for a skill and topics"""
    
    # Question templates that can be adapted for different skills
    question_templates = [
        {
            'template': 'What is the primary purpose of {skill}?',
            'type': 'multiple_choice',
            'category': 'concept'
        },
        {
            'template': 'Which of the following is a core feature of {skill}?',
            'type': 'multiple_choice',
            'category': 'features'
        },
        {
            'template': 'What is considered a best practice when working with {skill}?',
            'type': 'multiple_choice',
            'category': 'best_practices'
        },
        {
            'template': 'How would you debug a common {skill} error?',
            'type': 'multiple_choice',
            'category': 'troubleshooting'
        }
    ]
    
    # Skill-specific question banks
    skill_questions = {
        'python': [
            {
                'question': 'What is the correct way to define a function in Python?',
                'options': ['def function_name():', 'function function_name():', 'func function_name():', 'define function_name():'],
                'correct_answer': 'def function_name():',
                'explanation': 'Python uses the "def" keyword to define functions.'
            },
            {
                'question': 'Which data type is mutable in Python?',
                'options': ['tuple', 'string', 'list', 'int'],
                'correct_answer': 'list',
                'explanation': 'Lists are mutable in Python, meaning they can be changed after creation.'
            }
        ],
        'javascript': [
            {
                'question': 'What is the correct way to declare a variable in modern JavaScript?',
                'options': ['var myVar;', 'let myVar;', 'variable myVar;', 'declare myVar;'],
                'correct_answer': 'let myVar;',
                'explanation': 'In modern JavaScript, "let" is preferred for variable declaration.'
            },
            {
                'question': 'What does "=== " operator do in JavaScript?',
                'options': ['Assignment', 'Equality with type coercion', 'Strict equality', 'Not equal'],
                'correct_answer': 'Strict equality',
                'explanation': 'The === operator checks for strict equality without type conversion.'
            }
        ],
        'react': [
            {
                'question': 'What is JSX in React?',
                'options': ['A new programming language', 'JavaScript XML syntax extension', 'A CSS framework', 'A database query language'],
                'correct_answer': 'JavaScript XML syntax extension',
                'explanation': 'JSX is a syntax extension for JavaScript that allows writing HTML-like code in React.'
            },
            {
                'question': 'What is the purpose of React hooks?',
                'options': ['To style components', 'To manage state in functional components', 'To handle HTTP requests', 'To optimize performance'],
                'correct_answer': 'To manage state in functional components',
                'explanation': 'React hooks allow functional components to use state and other React features.'
            }
        ]
    }
    
    questions = []
    skill_lower = skill_name.lower()
    
    # Use skill-specific questions if available
    if skill_lower in skill_questions:
        questions.extend(skill_questions[skill_lower])
    
    # Generate additional questions from templates
    for i, topic in enumerate(topics[:3]):  # Limit to 3 topics per quiz
        if i < len(question_templates):
            template = question_templates[i]
            question = template['template'].format(skill=skill_name)
            
            # Generate generic options based on question type
            if template['category'] == 'concept':
                options = [
                    f'To provide a framework for building applications',
                    f'To manage data and state',
                    f'To create user interfaces',
                    f'To handle server-side logic'
                ]
            elif template['category'] == 'features':
                options = [
                    f'Component-based architecture',
                    f'Built-in database management',
                    f'Automatic code generation',
                    f'Hardware acceleration'
                ]
            else:
                options = [
                    f'Follow official documentation',
                    f'Use community best practices',
                    f'Regular testing and debugging',
                    f'All of the above'
                ]
            
            questions.append({
                'question': question,
                'options': options,
                'correct_answer': options[0],  # First option is usually correct
                'explanation': f'This relates to {topic.lower()} in {skill_name}.'
            })
    
    return questions[:5]  # Limit to 5 questions per quiz

# Main function to get everything
async def get_enhanced_resources_with_path(skill_name: str) -> Dict:
    """Get enhanced resources and generate a complete learning path"""
    
    # Get high-quality resources
    resources = await enhanced_resource_search(skill_name, max_results=12)
    
    # Generate learning path
    learning_path = generate_learning_path(skill_name, resources)
    
    return {
        'resources': resources,
        'learning_path': learning_path,
        'skill': skill_name,
        'total_resources': len(resources),
        'estimated_duration': learning_path['total_duration']
    }

# Fallback function for synchronous calls
def get_enhanced_resources_sync(skill_name: str) -> List[Dict]:
    """Synchronous wrapper for enhanced resource search"""
    try:
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(enhanced_resource_search(skill_name))
    except:
        # Fallback to basic search if async fails
        logger.warning(f"Enhanced search failed for {skill_name}, falling back to basic search")
        return basic_search(skill_name)
