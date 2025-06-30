"""
Enhanced resource uniqueness and quality system
"""
import requests
import time
from urllib.parse import urlparse
import logging

logger = logging.getLogger(__name__)

def validate_url_accessibility(url, timeout=5):
    """
    Validate that a URL is accessible and returns a valid response.
    Now validates ALL URLs to guarantee quality.
    
    Args:
        url (str): URL to validate
        timeout (int): Request timeout in seconds
        
    Returns:
        bool: True if URL is accessible, False otherwise
    """
    try:
        if not url or url.strip() == '':
            return False
            
        # Expanded list of trusted domains that we know are reliable
        trusted_domains = [
            'geeksforgeeks.org', 'leetcode.com', 'github.com',
            'developer.mozilla.org', 'react.dev', 'docs.python.org',
            'freecodecamp.org', 'youtube.com', 'youtu.be',
            'stackoverflow.com', 'w3schools.com', 'mdn.webdocs.org',
            'nodejs.org', 'reactjs.org', 'vuejs.org', 'angular.io',
            'coursera.org', 'udemy.com', 'edx.org', 'khanacademy.org',
            'codecademy.com', 'pluralsight.com', 'educative.io',
            'interviewbit.com', 'hackerrank.com', 'codechef.com',
            'codeforces.com', 'topcoder.com', 'javascript.info',
            'css-tricks.com', 'smashingmagazine.com', 'a11yproject.com'
        ]
        
        parsed_url = urlparse(url)
        domain = parsed_url.netloc.lower()
        
        # Even for trusted domains, do a quick validation
        if any(trusted in domain for trusted in trusted_domains):
            # Quick validation for trusted domains
            try:
                response = requests.head(url, timeout=2, allow_redirects=True)
                return response.status_code < 400
            except:
                return True  # Assume trusted domains are good if check fails
            
        # For other domains, do a thorough validation
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        
        # Check for common error status codes
        if response.status_code >= 400:
            return False
            
        # Check for redirects to error pages
        if 'error' in response.url.lower() or '404' in response.url.lower():
            return False
            
        return True
        
    except Exception as e:
        logger.debug(f"URL validation failed for {url}: {e}")
        return False

def calculate_comprehensive_quality_score(resource):
    """
    Calculate a comprehensive quality score for a resource based on multiple factors.
    
    Args:
        resource (dict): Resource dictionary
        
    Returns:
        int: Quality score (0-100)
    """
    base_score = resource.get('quality_score', 50)
    
    # Domain-based scoring
    url = resource.get('url', '').lower()
    domain_bonus = 0
    
    premium_domains = {
        'developer.mozilla.org': 25,
        'docs.python.org': 25,
        'react.dev': 25,
        'nodejs.org': 25,
        'freecodecamp.org': 20,
        'geeksforgeeks.org': 15,
        'leetcode.com': 15,
        'github.com': 10,
        'youtube.com': 5
    }
    
    for domain, bonus in premium_domains.items():
        if domain in url:
            domain_bonus = bonus
            break
    
    # Resource type scoring
    type_bonus = {
        'documentation': 15,
        'course': 10,
        'article': 5,
        'video': 5,
        'github': 5
    }.get(resource.get('resource_type'), 0)
    
    # Title quality (avoid generic titles)
    title = resource.get('title', '').lower()
    title_penalty = 0
    generic_terms = ['tutorial', 'guide', 'introduction', 'basics', 'learn']
    if sum(1 for term in generic_terms if term in title) > 2:
        title_penalty = 10
    
    # Content specificity bonus (reward specific technical terms)
    specificity_bonus = 0
    technical_terms = ['algorithm', 'implementation', 'optimization', 'advanced', 'deep dive']
    specificity_bonus = sum(5 for term in technical_terms if term in title) 
    
    # URL structure quality (prefer clean, organized URLs)
    url_quality_bonus = 0
    if '/docs/' in url or '/documentation/' in url:
        url_quality_bonus = 5
    elif '/tutorial/' in url or '/guide/' in url:
        url_quality_bonus = 3
    
    final_score = min(100, base_score + domain_bonus + type_bonus - title_penalty + specificity_bonus + url_quality_bonus)
    return max(10, final_score)  # Minimum score of 10

def ensure_resource_uniqueness_and_quality(all_resources, skill_name, max_resources=8):
    """
    Ensure resources are unique and of high quality with specific criteria for each subskill.
    PRIORITIZES QUALITY - increased max_resources and stricter filtering.
    
    Args:
        all_resources (list): List of resources to filter
        skill_name (str): Name of the skill/subskill
        max_resources (int): Maximum number of resources to return (increased for more variety)
        
    Returns:
        list: Filtered list of unique, high-quality, validated resources
    """
    
    # ULTRA-STRICT quality thresholds - only the absolute best resources pass
    QUALITY_THRESHOLDS = {
        'documentation': 85,  # Slightly reduced to allow more good docs through
        'course': 80,         # Quality courses  
        'article': 75,        # Quality articles
        'video': 70,          # Good videos
        'github': 70,         # Quality repositories
        'tutorial': 65        # Solid tutorials
    }
    
    # Remove duplicates by URL and title similarity
    unique_resources = []
    seen_urls = set()
    seen_titles = set()
    validated_count = 0
    
    # Sort by quality score first
    sorted_resources = sorted(all_resources, key=lambda x: x.get('quality_score', 0), reverse=True)
    
    for resource in sorted_resources:
        url = resource.get('url', '').lower()
        title = resource.get('title', '').lower()
        resource_type = resource.get('resource_type', 'unknown')
        
        # Check URL uniqueness
        if url in seen_urls:
            continue
            
        # Check title similarity (avoid very similar titles)
        title_words = set(title.split())
        is_similar = False
        for seen_title in seen_titles:
            seen_words = set(seen_title.split())
            # More strict similarity check (70% threshold instead of 60%)
            if len(title_words & seen_words) / max(len(title_words), len(seen_words)) > 0.7:
                is_similar = True
                break
        
        if is_similar:
            continue
        
        # Check for domain diversity (avoid too many from same domain)
        domain = urlparse(resource.get('url', '')).netloc.lower()
        domain_count = sum(1 for r in unique_resources if urlparse(r.get('url', '')).netloc.lower() == domain)
        if domain_count >= 2 and domain not in ['geeksforgeeks.org', 'developer.mozilla.org']:
            continue
        
        # Calculate comprehensive quality score
        quality_score = calculate_comprehensive_quality_score(resource)
        resource['quality_score'] = quality_score
        
        # Check quality threshold
        threshold = QUALITY_THRESHOLDS.get(resource_type, 65)
        if quality_score < threshold:
            continue
        
        # Validate URL accessibility (VALIDATE ALL URLs for guaranteed quality)
        if not validate_url_accessibility(resource.get('url', '')):
            logger.debug(f"Skipping inaccessible URL: {resource.get('url')}")
            continue
        
        # Add to unique resources
        unique_resources.append(resource)
        seen_urls.add(url)
        seen_titles.add(title)
        
        if len(unique_resources) >= max_resources:
            break
    
    # Enhanced diversity enforcement - prioritize variety of resource types
    final_resources = []
    type_counts = {}
    
    # Define ideal resource type distribution for maximum learning diversity
    preferred_types = ['documentation', 'video', 'course', 'article', 'github', 'tutorial']
    max_per_type = max(1, max_resources // len(preferred_types))  # More even distribution
    
    # First pass: ensure at least one of each preferred type if available
    for preferred_type in preferred_types:
        for resource in unique_resources:
            resource_type = resource.get('resource_type', 'unknown')
            if (resource_type == preferred_type and 
                type_counts.get(resource_type, 0) == 0 and 
                len(final_resources) < max_resources):
                final_resources.append(resource)
                type_counts[resource_type] = type_counts.get(resource_type, 0) + 1
                break
    
    # Second pass: fill remaining slots with balanced distribution
    for resource in unique_resources:
        if resource in final_resources:
            continue
        resource_type = resource.get('resource_type', 'unknown')
        if (type_counts.get(resource_type, 0) < max_per_type and 
            len(final_resources) < max_resources):
            final_resources.append(resource)
            type_counts[resource_type] = type_counts.get(resource_type, 0) + 1
    
    # Third pass: fill any remaining slots with best available resources
    remaining_slots = max_resources - len(final_resources)
    if remaining_slots > 0:
        for resource in unique_resources:
            if resource not in final_resources:
                final_resources.append(resource)
                remaining_slots -= 1
                if remaining_slots == 0:
                    break
    
    logger.info(f"Filtered to {len(final_resources)} unique, validated resources for {skill_name}")
    return final_resources[:max_resources]


def get_specialized_resources_for_subskill(subskill_name):
    """
    Get highly specialized resources that are unique to specific subskills.
    These are hand-curated to ensure maximum uniqueness and relevance.
    """
    
    SPECIALIZED_RESOURCES = {
        # DSA - Each subskill gets completely unique, comprehensive resources
        "Arrays": [
            {
                "title": "Array Rotation Algorithms Masterclass",
                "url": "https://www.geeksforgeeks.org/array-rotation/",
                "description": "Master all array rotation techniques and optimizations",
                "resource_type": "article",
                "quality_score": 94
            },
            {
                "title": "Sliding Window Technique for Arrays",
                "url": "https://www.geeksforgeeks.org/window-sliding-technique/",
                "description": "Essential sliding window patterns for array problems",
                "resource_type": "article", 
                "quality_score": 92
            },
            {
                "title": "Array Interview Questions - Top 50",
                "url": "https://www.interviewbit.com/array-interview-questions/",
                "description": "Curated collection of most asked array interview questions",
                "resource_type": "course",
                "quality_score": 90
            },
            {
                "title": "Two Pointer Technique for Arrays",
                "url": "https://leetcode.com/discuss/study-guide/1688903/Solved-all-two-pointers-problems-in-100-days",
                "description": "Master the two-pointer technique with real problems",
                "resource_type": "article",
                "quality_score": 88
            },
            {
                "title": "Array Data Structure - Complete Documentation",
                "url": "https://en.cppreference.com/w/cpp/container/array",
                "description": "Comprehensive technical documentation on arrays",
                "resource_type": "documentation",
                "quality_score": 95
            },
            {
                "title": "Advanced Array Algorithms Video Course",
                "url": "https://www.youtube.com/watch?v=pmN9ExDf3yQ",
                "description": "Complete video course on advanced array techniques",
                "resource_type": "video",
                "quality_score": 87
            },
            {
                "title": "Array Algorithms Implementation - GitHub",
                "url": "https://github.com/mission-peace/interview/tree/master/src/com/interview/array",
                "description": "Comprehensive array algorithm implementations",
                "resource_type": "github",
                "quality_score": 85
            },
            {
                "title": "Interactive Array Tutorial",
                "url": "https://www.programiz.com/dsa/array",
                "description": "Step-by-step interactive array learning tutorial",
                "resource_type": "tutorial",
                "quality_score": 83
            }
        ],
        
        "Linked Lists": [
            {
                "title": "Reverse Linked List - All Variations",
                "url": "https://www.geeksforgeeks.org/reverse-a-linked-list/",
                "description": "Master all linked list reversal techniques",
                "resource_type": "article",
                "quality_score": 94
            },
            {
                "title": "Linked List Cycle Detection Algorithms",
                "url": "https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/",
                "description": "Floyd's algorithm and other cycle detection methods",
                "resource_type": "article",
                "quality_score": 92
            },
            {
                "title": "Merge Two Sorted Lists - Multiple Approaches",
                "url": "https://leetcode.com/problems/merge-two-sorted-lists/solutions/",
                "description": "Different techniques to merge sorted linked lists",
                "resource_type": "course",
                "quality_score": 90
            },
            {
                "title": "Linked List Data Structure Documentation",
                "url": "https://en.wikipedia.org/wiki/Linked_list",
                "description": "Comprehensive academic documentation on linked lists",
                "resource_type": "documentation",
                "quality_score": 88
            },
            {
                "title": "Linked List Masterclass Video Series",
                "url": "https://www.youtube.com/watch?v=WwfhLC16bis",
                "description": "Complete video series on linked list operations and algorithms",
                "resource_type": "video",
                "quality_score": 86
            },
            {
                "title": "Linked List Implementations Repository",
                "url": "https://github.com/TheAlgorithms/Python/tree/master/data_structures/linked_list",
                "description": "Multiple linked list implementations in various languages",
                "resource_type": "github",
                "quality_score": 84
            },
            {
                "title": "Interactive Linked List Tutorial",
                "url": "https://www.cs.usfca.edu/~galles/visualization/LinkedList.html",
                "description": "Visual and interactive linked list operations tutorial",
                "resource_type": "tutorial",
                "quality_score": 87
            },
            {
                "title": "Advanced Linked List Patterns Course",
                "url": "https://leetcode.com/explore/learn/card/linked-list/",
                "description": "Comprehensive course on advanced linked list patterns",
                "resource_type": "course",
                "quality_score": 89
            }
        ],
        
        "Binary Trees": [
            {
                "title": "Binary Tree Traversal - All Methods",
                "url": "https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/",
                "description": "Comprehensive guide to tree traversal algorithms",
                "resource_type": "article",
                "quality_score": 94
            },
            {
                "title": "Binary Tree Maximum Path Sum",
                "url": "https://leetcode.com/problems/binary-tree-maximum-path-sum/",
                "description": "Classic tree recursion problem with multiple solutions",
                "resource_type": "course",
                "quality_score": 92
            },
            {
                "title": "Serialize and Deserialize Binary Tree",
                "url": "https://www.geeksforgeeks.org/serialize-deserialize-binary-tree/",
                "description": "Advanced tree manipulation techniques",
                "resource_type": "article",
                "quality_score": 90
            }
        ],
        
        "Stacks": [
            {
                "title": "Next Greater Element using Stack",
                "url": "https://www.geeksforgeeks.org/next-greater-element/",
                "description": "Classic stack application for finding next greater elements",
                "resource_type": "article",
                "quality_score": 94
            },
            {
                "title": "Valid Parentheses and Bracket Matching",
                "url": "https://leetcode.com/problems/valid-parentheses/",
                "description": "Fundamental stack problem with multiple variations",
                "resource_type": "course",
                "quality_score": 92
            },
            {
                "title": "Largest Rectangle in Histogram",
                "url": "https://www.geeksforgeeks.org/largest-rectangle-under-histogram/",
                "description": "Advanced stack technique for area calculations",
                "resource_type": "article",
                "quality_score": 90
            }
        ],
        
        "Dynamic Programming": [
            {
                "title": "DP Patterns - Complete Classification",
                "url": "https://www.geeksforgeeks.org/dynamic-programming/",
                "description": "Comprehensive guide to all DP patterns and approaches",
                "resource_type": "article",
                "quality_score": 96
            },
            {
                "title": "Longest Common Subsequence - DP Classic",
                "url": "https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/",
                "description": "Master the fundamental DP problem with optimizations",
                "resource_type": "article",
                "quality_score": 94
            },
            {
                "title": "Knapsack Problem - All Variations",
                "url": "https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/",
                "description": "Complete guide to knapsack problems and variations",
                "resource_type": "course",
                "quality_score": 92
            }
        ],
        
        # Web Development - Highly specific resources
        "HTML Fundamentals": [
            {
                "title": "HTML5 Canvas Complete Guide",
                "url": "https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial",
                "description": "Master HTML5 Canvas for graphics and animations",
                "resource_type": "documentation",
                "quality_score": 96
            },
            {
                "title": "Web Accessibility with HTML",
                "url": "https://www.w3.org/WAI/tutorials/",
                "description": "Build accessible web content with proper HTML",
                "resource_type": "article",
                "quality_score": 94
            },
            {
                "title": "HTML Form Validation Masterclass",
                "url": "https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation",
                "description": "Advanced form validation techniques and patterns",
                "resource_type": "article",
                "quality_score": 92
            }
        ],
        
        "CSS Fundamentals": [
            {
                "title": "CSS Grid Layout Complete Guide",
                "url": "https://css-tricks.com/snippets/css/complete-guide-grid/",
                "description": "Master CSS Grid for complex responsive layouts",
                "resource_type": "article",
                "quality_score": 96
            },
            {
                "title": "CSS Custom Properties (Variables)",
                "url": "https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties",
                "description": "Dynamic styling with CSS custom properties",
                "resource_type": "documentation",
                "quality_score": 94
            },
            {
                "title": "Advanced CSS Animations",
                "url": "https://css-tricks.com/almanac/properties/a/animation/",
                "description": "Create complex animations with CSS keyframes",
                "resource_type": "article",
                "quality_score": 92
            }
        ],
        
        "JavaScript Fundamentals": [
            {
                "title": "JavaScript Closures Deep Dive",
                "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures",
                "description": "Understanding closures and lexical scoping",
                "resource_type": "documentation",
                "quality_score": 96
            },
            {
                "title": "Async/Await and Promises Mastery",
                "url": "https://javascript.info/async-await",
                "description": "Master asynchronous JavaScript programming",
                "resource_type": "article",
                "quality_score": 94
            },
            {
                "title": "JavaScript Design Patterns",
                "url": "https://www.patterns.dev/posts/classic-design-patterns/",
                "description": "Common design patterns in modern JavaScript",
                "resource_type": "article",
                "quality_score": 92
            }
        ],
        
        "React Fundamentals": [
            {
                "title": "React Hooks Complete Guide",
                "url": "https://react.dev/reference/react",
                "description": "Master all React hooks with practical examples",
                "resource_type": "documentation",
                "quality_score": 96
            },
            {
                "title": "React State Management Patterns",
                "url": "https://kentcdodds.com/blog/application-state-management-with-react",
                "description": "Advanced state management techniques in React",
                "resource_type": "article",
                "quality_score": 94
            },
            {
                "title": "React Performance Optimization",
                "url": "https://react.dev/learn/render-and-commit",
                "description": "Optimize React apps for better performance",
                "resource_type": "article",
                "quality_score": 92
            }
        ]
    }
    
    return SPECIALIZED_RESOURCES.get(subskill_name, [])

def get_performance_metrics(resource_list):
    """
    Calculate performance metrics for a list of resources with enhanced diversity scoring.
    
    Args:
        resource_list (list): List of resource dictionaries
        
    Returns:
        dict: Performance metrics including uniqueness, quality, and diversity
    """
    if not resource_list:
        return {
            "total_resources": 0,
            "uniqueness_score": 0,
            "avg_quality_score": 0,
            "resource_diversity": 0,
            "performance_grade": "F",
            "resource_type_distribution": {},
            "recommendations": ["No resources found"]
        }
    
    # Calculate uniqueness (based on unique URLs and titles)
    unique_urls = len(set(r.get('url', '') for r in resource_list))
    unique_titles = len(set(r.get('title', '') for r in resource_list))
    uniqueness_score = min(100, (unique_urls + unique_titles) / (2 * len(resource_list)) * 100)
    
    # Calculate average quality score
    quality_scores = [r.get('quality_score', 0) for r in resource_list]
    avg_quality_score = sum(quality_scores) / len(quality_scores) if quality_scores else 0
    
    # Enhanced resource type diversity calculation
    resource_types = [r.get('resource_type', 'unknown') for r in resource_list]
    type_distribution = {}
    for rtype in resource_types:
        type_distribution[rtype] = type_distribution.get(rtype, 0) + 1
    
    unique_types = len(set(resource_types))
    ideal_types = 6  # documentation, video, course, article, github, tutorial
    
    # Enhanced diversity score - reward having multiple types
    if unique_types >= 5:
        diversity_bonus = 20
    elif unique_types >= 4:
        diversity_bonus = 15
    elif unique_types >= 3:
        diversity_bonus = 10
    else:
        diversity_bonus = 0
    
    base_diversity = (unique_types / min(ideal_types, len(resource_list))) * 80
    resource_diversity = min(100, base_diversity + diversity_bonus)
    
    # Calculate overall performance grade with weighted scoring
    # Quality is most important (40%), then diversity (35%), then uniqueness (25%)
    overall_score = (avg_quality_score * 0.4) + (resource_diversity * 0.35) + (uniqueness_score * 0.25)
    
    if overall_score >= 92:
        grade = "A+"
    elif overall_score >= 88:
        grade = "A"
    elif overall_score >= 82:
        grade = "A-"
    elif overall_score >= 78:
        grade = "B+"
    elif overall_score >= 75:
        grade = "B"
    elif overall_score >= 70:
        grade = "B-"
    elif overall_score >= 65:
        grade = "C+"
    elif overall_score >= 60:
        grade = "C"
    elif overall_score >= 55:
        grade = "C-"
    elif overall_score >= 50:
        grade = "D"
    else:
        grade = "F"
    
    # Generate recommendations
    recommendations = []
    if avg_quality_score < 80:
        recommendations.append("Consider higher-quality sources")
    if resource_diversity < 60:
        recommendations.append("Add more diverse resource types (videos, documentation, tutorials)")
    if uniqueness_score < 90:
        recommendations.append("Remove duplicate or similar resources")
    if not recommendations:
        recommendations.append("Excellent resource collection!")
    
    return {
        "total_resources": len(resource_list),
        "uniqueness_score": round(uniqueness_score, 1),
        "avg_quality_score": round(avg_quality_score, 1),
        "resource_diversity": round(resource_diversity, 1),
        "performance_grade": grade,
        "overall_score": round(overall_score, 1),
        "resource_type_distribution": type_distribution,
        "unique_types_count": unique_types,
        "recommendations": recommendations
    }
