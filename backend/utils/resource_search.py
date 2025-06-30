"""
Utility functions for dynamically searching and retrieving resource links
without using paid APIs or API keys. Enhanced with quality scoring.
"""
import requests
from bs4 import BeautifulSoup
import random
import time
import re
import logging
from .curated_resources import get_curated_resources, calculate_resource_quality
from .fast_fallback import get_fast_fallback_resources
from .enhanced_uniqueness import ensure_resource_uniqueness_and_quality, get_specialized_resources_for_subskill
from .robust_resource_fetcher import get_robust_resources

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Headers to mimic a browser visit with shorter timeout
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.google.com/',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

# Timeout settings for faster response
REQUEST_TIMEOUT = 2  # Reduced from 3 to 2 seconds for faster response
MAX_RETRIES = 1      # Reduced retries for faster response

# Resource caching for improved performance
_resource_cache = {}
CACHE_EXPIRY = 3600  # 1 hour cache

def get_cached_resources(cache_key):
    """Get resources from cache if available and not expired"""
    if cache_key in _resource_cache:
        cached_data, timestamp = _resource_cache[cache_key]
        if time.time() - timestamp < CACHE_EXPIRY:
            return cached_data
    return None

def cache_resources(cache_key, resources):
    """Cache resources with timestamp"""
    _resource_cache[cache_key] = (resources, time.time())

def extract_youtube_metadata(soup, video_id=None):
    """
    Extract metadata like view count and engagement from YouTube page.
    
    Args:
        soup: BeautifulSoup object of the page
        video_id: YouTube video ID (optional)
        
    Returns:
        dict: Metadata including view_count, likes, etc.
    """
    metadata = {'view_count': 0, 'likes': 0}
    
    try:
        # Try to extract view count from various selectors
        view_selectors = [
            'span.view-count',
            '.view-count',
            '[class*="viewCount"]',
            '.ytd-video-view-count-renderer'
        ]
        
        for selector in view_selectors:
            view_element = soup.select_one(selector)
            if view_element:
                view_text = view_element.get_text()
                # Extract numbers from view count (e.g., "1.2M views" -> 1200000)
                view_match = re.search(r'([\d,\.]+)', view_text)
                if view_match:
                    view_str = view_match.group(1).replace(',', '')
                    if 'K' in view_text:
                        metadata['view_count'] = int(float(view_str) * 1000)
                    elif 'M' in view_text:
                        metadata['view_count'] = int(float(view_str) * 1000000)
                    else:
                        metadata['view_count'] = int(float(view_str))
                break
    
    except Exception as e:
        logger.debug(f"Error extracting YouTube metadata: {e}")
    
    return metadata

def get_youtube_videos(query, max_results=3):
    """
    Search YouTube for videos related to the query.
    
    Args:
        query (str): Search query
        max_results (int): Maximum number of results to return
        
    Returns:
        list: List of dictionaries containing video title, URL, and description
    """
    try:
        # Construct the search URL
        search_query = query.replace(' ', '+')
        url = f"https://www.youtube.com/results?search_query={search_query}"
          # Send request with timeout
        response = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
        if response.status_code != 200:
            logger.warning(f"Failed to fetch YouTube results: {response.status_code}")
            return []
        
        # Parse with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract video information
        videos = []
        
        # Method 1: Try to extract from initial data
        script_tag = soup.find("script", text=re.compile("var ytInitialData"))
        if script_tag:
            # Extract the JSON data
            data_str = script_tag.string
            start_idx = data_str.find('var ytInitialData = ') + len('var ytInitialData = ')
            end_idx = data_str.find('};', start_idx) + 1
            json_str = data_str[start_idx:end_idx]
              # Extract video IDs using regex
            video_ids = re.findall(r'"videoId":"([^"]+)"', json_str)[:max_results]
            video_titles = re.findall(r'"title":{"runs":\[{"text":"([^"]+)"}]}', json_str)[:max_results]
            # Create result list with quality scoring
            for i, video_id in enumerate(video_ids):
                if i < len(video_titles):
                    title = video_titles[i]
                else:
                    title = f"Video about {query}"
                    
                url = f"https://www.youtube.com/watch?v={video_id}"
                description = f"YouTube video about {query}"
                
                # Calculate quality score
                quality_score = calculate_resource_quality(
                    title, description, url, domain_bonus=False
                )
                
                videos.append({
                    'title': title,
                    'url': url,
                    'description': description,
                    'resource_type': 'video',
                    'quality_score': quality_score
                })
                
                if len(videos) >= max_results:
                    break
        
        # Method 2: If method 1 fails, try finding video links directly
        if not videos:
            video_elements = soup.select('a.yt-uix-tile-link') or soup.select('a#video-title')
            for element in video_elements:
                if element.has_attr('href') and element.has_attr('title'):
                    href = element['href']
                    # Only process video links
                    if href.startswith('/watch'):
                        url = f"https://www.youtube.com{href}"
                        title = element['title']
                        videos.append({
                            'title': title,
                            'url': url,
                            'description': f"YouTube video about {query}",
                            'resource_type': 'video'
                        })
                        
                        if len(videos) >= max_results:
                            break
        
        # Method 3: Fallback to a simple pattern search if all else fails
        if not videos:
            video_pattern = re.compile(r'/watch\?v=([a-zA-Z0-9_-]+)')
            matches = video_pattern.findall(response.text)
              # Deduplicate
            unique_ids = list(set(matches))[:max_results]
            
            for video_id in unique_ids:
                url = f"https://www.youtube.com/watch?v={video_id}"
                videos.append({
                    'title': f"{query.capitalize()} Tutorial",
                    'url': url,
                    'description': f"YouTube video about {query}",
                    'resource_type': 'video'
                })
        
        return videos[:max_results]
        
    except requests.exceptions.Timeout:
        logger.warning(f"YouTube search timed out for query: {query}")
        return []
    except Exception as e:
        logger.error(f"Error fetching YouTube videos: {str(e)}")
        return []

def get_articles(query, max_results=3):
    """
    Search for articles related to the query with improved rate limiting handling.
    
    Args:
        query (str): Search query
        max_results (int): Maximum number of results to return
        
    Returns:
        list: List of dictionaries containing article title, URL, and description
    """
    try:
        # Multiple search strategies to avoid rate limiting
        search_strategies = [
            ("https://html.duckduckgo.com/html/?q={query}+tutorial", "DuckDuckGo"),
            ("https://www.bing.com/search?q={query}+tutorial", "Bing"),
            ("https://startpage.com/sp/search?q={query}+tutorial", "Startpage")
        ]
        
        for url_template, engine_name in search_strategies:
            try:
                # Construct the search URL
                search_query = query.replace(' ', '+')
                url = url_template.format(query=search_query)
                
                # Add random delay to avoid rate limiting
                time.sleep(random.uniform(0.5, 1.5))
                
                # Send request with timeout
                response = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
                if response.status_code == 202:
                    logger.warning(f"{engine_name} returned 202 (rate limited), trying next engine")
                    continue
                elif response.status_code != 200:
                    logger.warning(f"Failed to fetch {engine_name} results: {response.status_code}")
                    continue
                
                # Parse with BeautifulSoup
                soup = BeautifulSoup(response.text, 'html.parser')
                articles = []
                
                # Engine-specific parsing
                if engine_name == "DuckDuckGo":
                    articles = _parse_duckduckgo_results(soup, query, max_results)
                elif engine_name == "Bing":
                    articles = _parse_bing_results(soup, query, max_results)
                elif engine_name == "Startpage":
                    articles = _parse_startpage_results(soup, query, max_results)
                
                if articles:
                    logger.info(f"Successfully got {len(articles)} articles from {engine_name}")
                    return articles
                    
            except requests.exceptions.Timeout:
                logger.warning(f"{engine_name} search timed out for query: {query}")
                continue
            except Exception as e:
                logger.error(f"Error with {engine_name} search: {str(e)}")
                continue
        
        # If all engines fail, return empty list
        logger.warning(f"All search engines failed for query: {query}")
        return []
        
    except Exception as e:
        logger.error(f"Error in get_articles: {str(e)}")
        return []

def _parse_duckduckgo_results(soup, query, max_results):
    """Parse DuckDuckGo search results."""
    articles = []
    result_elements = soup.select('.result')
    
    for element in result_elements:
        title_element = element.select_one('.result__a')
        snippet_element = element.select_one('.result__snippet')
        
        if title_element and title_element.has_attr('href'):
            href = title_element['href']
            
            # Extract the actual URL from DuckDuckGo redirect URL
            actual_url = href
            if 'uddg=' in href:
                actual_url = requests.utils.unquote(href.split('uddg=')[1].split('&')[0])
            title = title_element.get_text().strip()
            description = snippet_element.get_text().strip() if snippet_element else f"Article about {query}"
            
            # Skip YouTube results and ads
            if 'youtube.com' in actual_url or 'ad_domain' in href or '/y.js?' in href:
                continue
            
            # Calculate quality score
            quality_score = calculate_resource_quality(
                title, description, actual_url, domain_bonus=True
            )
            
            articles.append({
                'title': title,
                'url': actual_url,
                'description': description,
                'resource_type': 'article',
                'quality_score': quality_score
            })
            
            if len(articles) >= max_results:
                break
    
    return articles

def _parse_bing_results(soup, query, max_results):
    """Parse Bing search results."""
    articles = []
    result_elements = soup.select('li.b_algo')
    
    for element in result_elements:
        title_element = element.select_one('h2 a')
        snippet_element = element.select_one('.b_caption p')
        
        if title_element:
            title = title_element.get_text().strip()
            url = title_element.get('href', '')
            description = snippet_element.get_text().strip() if snippet_element else f"Article about {query}"
            
            # Skip YouTube results
            if 'youtube.com' in url:
                continue
            
            quality_score = calculate_resource_quality(title, description, url, domain_bonus=True)
            
            articles.append({
                'title': title,
                'url': url,
                'description': description,
                'resource_type': 'article',
                'quality_score': quality_score
            })
            
            if len(articles) >= max_results:
                break
    
    return articles

def _parse_startpage_results(soup, query, max_results):
    """Parse Startpage search results."""
    articles = []
    result_elements = soup.select('.w-gl__result')
    
    for element in result_elements:
        title_element = element.select_one('h3 a')
        snippet_element = element.select_one('.w-gl__description')
        
        if title_element:
            title = title_element.get_text().strip()
            url = title_element.get('href', '')
            description = snippet_element.get_text().strip() if snippet_element else f"Article about {query}"
            
            # Skip YouTube results
            if 'youtube.com' in url:
                continue
            
            quality_score = calculate_resource_quality(title, description, url, domain_bonus=True)
            
            articles.append({
                'title': title,
                'url': url,
                'description': description,
                'resource_type': 'article',
                'quality_score': quality_score
            })
            
            if len(articles) >= max_results:
                break
    
    return articles

def get_github_repos(query, max_results=3):
    """
    Search GitHub for repositories related to the query.
    
    Args:
        query (str): Search query
        max_results (int): Maximum number of results to return
        
    Returns:
        list: List of dictionaries containing repo title, URL, and description
    """
    try:
        # Construct the search URL
        search_query = query.replace(' ', '+')
        url = f"https://github.com/search?q={search_query}&type=repositories"
          # Send request with timeout
        response = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
        if response.status_code != 200:
            logger.warning(f"Failed to fetch GitHub results: {response.status_code}")
            return []
        
        # Parse with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract repository information
        repos = []
        
        # Find all repository elements
        repo_elements = soup.select('.repo-list-item')
        
        for element in repo_elements:
            title_element = element.select_one('.f4')
            description_element = element.select_one('.mb-1')
            
            if title_element and title_element.find('a'):
                href = title_element.find('a')['href']
                url = f"https://github.com{href}"
                title = title_element.get_text().strip()
                description = description_element.get_text().strip() if description_element else f"GitHub repository about {query}"
                
                # Calculate quality score
                quality_score = calculate_resource_quality(
                    title, description, url, domain_bonus=True
                )
                
                repos.append({
                    'title': title,
                    'url': url,
                    'description': description,
                    'resource_type': 'github',
                    'quality_score': quality_score
                })
                
                if len(repos) >= max_results:
                    break
        return repos[:max_results]
        
    except requests.exceptions.Timeout:
        logger.warning(f"GitHub search timed out for query: {query}")
        return []
    except Exception as e:
        logger.error(f"Error fetching GitHub repos: {str(e)}")
        return []

def get_resources_for_skill(skill_name, resource_types=None, max_per_type=4):
    """
    Get high-quality resources for a skill, prioritizing subskill-specific content and quality scores.
    Now focuses on QUALITY over speed - fetches more resources per subskill.
    
    Args:
        skill_name (str): Name of the skill
        resource_types (list): List of resource types to search for (default: all types)
        max_per_type (int): Maximum number of resources per type (increased default for quality)
        
    Returns:
        list: List of high-quality resource dictionaries, sorted by quality score
    """
    # Check cache first
    cache_key = f"{skill_name}_{max_per_type}"
    cached_result = get_cached_resources(cache_key)
    if cached_result:
        logger.info(f"Returning cached resources for {skill_name}")
        return cached_result
    
    if resource_types is None:
        # Extended list of resource types for maximum diversity
        resource_types = ['documentation', 'video', 'course', 'article', 'github', 'tutorial']

    all_resources = []
    
    # Increased target total for more comprehensive resources
    target_total = len(resource_types) * max_per_type * 2  # Fetch double to ensure quality filtering works
    
    # Enhanced subskill detection - check for exact subskill matches first
    skill_lower = skill_name.lower().strip()
    
    # Define subskill mapping for better resource matching
    SUBSKILL_MAPPING = {
        # DSA Subskills
        'arrays': 'Arrays',
        'array': 'Arrays', 
        'linked lists': 'Linked Lists',
        'linked list': 'Linked Lists',
        'binary trees': 'Binary Trees',
        'binary tree': 'Binary Trees',
        'tree': 'Binary Trees',
        'trees': 'Binary Trees',
        'binary search trees': 'Binary Search Trees',
        'binary search tree': 'Binary Search Trees',
        'bst': 'Binary Search Trees',
        'stacks': 'Stacks',
        'stack': 'Stacks',
        'queues': 'Queues', 
        'queue': 'Queues',
        'graphs': 'Graphs',
        'graph': 'Graphs',
        'dynamic programming': 'Dynamic Programming',
        'dp': 'Dynamic Programming',
        'sorting algorithms': 'Sorting Algorithms',
        'sorting': 'Sorting Algorithms',
        'searching algorithms': 'Searching Algorithms',
        'searching': 'Searching Algorithms',
        'binary search': 'Searching Algorithms',
        
        # Web Development Subskills
        'html fundamentals': 'HTML Fundamentals',
        'html basics': 'HTML Fundamentals',
        'html': 'HTML Fundamentals',
        'css fundamentals': 'CSS Fundamentals', 
        'css basics': 'CSS Fundamentals',
        'css': 'CSS Fundamentals',
        'javascript fundamentals': 'JavaScript Fundamentals',
        'javascript basics': 'JavaScript Fundamentals',
        'javascript': 'JavaScript Fundamentals',
        'js': 'JavaScript Fundamentals',
        'react fundamentals': 'React Fundamentals',
        'react basics': 'React Fundamentals', 
        'react': 'React Fundamentals',
        'node.js backend': 'Node.js Backend',
        'node.js': 'Node.js Backend',
        'nodejs': 'Node.js Backend',
        'express': 'Node.js Backend',
        
        # Machine Learning Subskills
        'linear algebra for ml': 'Linear Algebra for ML',
        'linear algebra': 'Linear Algebra for ML',
        'statistics for ml': 'Statistics for ML',
        'statistics': 'Statistics for ML',
        'supervised learning': 'Supervised Learning',
        'deep learning': 'Deep Learning',
        'neural networks': 'Deep Learning',
        
        # Python Subskills
        'python basics': 'Python Basics',
        'python fundamentals': 'Python Basics',
        'object-oriented programming': 'Object-Oriented Programming',
        'oop': 'Object-Oriented Programming',
        'python oop': 'Object-Oriented Programming',
        'python libraries': 'Python Libraries',
        'numpy': 'Python Libraries',
        'pandas': 'Python Libraries',
        'matplotlib': 'Python Libraries'
    }
    
    # Check for exact subskill match
    matched_subskill = SUBSKILL_MAPPING.get(skill_lower)
    if matched_subskill:
        logger.info(f"Found specific subskill match: '{skill_name}' -> '{matched_subskill}'")
        
        # First, get specialized resources for maximum uniqueness
        specialized_resources = get_specialized_resources_for_subskill(matched_subskill)
        if specialized_resources:
            all_resources.extend(specialized_resources)
            logger.info(f"Added {len(specialized_resources)} specialized resources for {matched_subskill}")
        
        # Then get additional subskill resources from fast fallback
        subskill_resources = get_fast_fallback_resources(matched_subskill)
        if subskill_resources:
            all_resources.extend(subskill_resources)
            logger.info(f"Added {len(subskill_resources)} fallback resources for {matched_subskill}")
    
    # Apply enhanced uniqueness and quality filtering
    if all_resources:
        all_resources = ensure_resource_uniqueness_and_quality(all_resources, skill_name, target_total)
    
    # Special handling for main DSA skills - only add Striver's DSA Sheet for main DSA searches, not subskills
    dsa_main_terms = ['data structure and algorithm', 'data structures and algorithms', 'dsa', 'algorithms and data structures']
    dsa_subskill_terms = ['array', 'linked list', 'stack', 'queue', 'tree', 'graph', 'sorting', 'searching', 'dynamic programming', 'greedy']
    
    # Only add Striver's DSA Sheet if it's a main DSA skill, not a specific subskill
    is_main_dsa_skill = any(term in skill_lower for term in dsa_main_terms)
    is_dsa_subskill = any(term in skill_lower for term in dsa_subskill_terms)
    
    if is_main_dsa_skill and not is_dsa_subskill:
        striver_resource = {
            "title": "Striver's A2Z DSA Course/Sheet",
            "url": "https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/",
            "description": "Comprehensive step-by-step DSA sheet by Striver - most popular DSA preparation resource",
            "resource_type": "course",
            "quality_score": 98
        }
        all_resources.append(striver_resource)
        logger.info(f"Added Striver's DSA Sheet for main DSA skill: {skill_name}")

    # Step 1: Try to get curated resources if no specific subskill match
    if not matched_subskill:
        curated_resources = get_curated_resources(skill_name)
        
        if curated_resources:
            logger.info(f"Found {len(curated_resources)} curated resources for {skill_name}")
            for resource in curated_resources:
                # Ensure resource has a quality score
                if 'quality_score' not in resource:
                    resource['quality_score'] = calculate_resource_quality(
                        resource.get('title', ''),
                        resource.get('description', ''),
                        resource.get('url', ''),
                        domain_bonus=True
                    )
                all_resources.append(resource)
    
    # Step 1.5: Always try fast fallback first for speed
    fallback_resources = get_fast_fallback_resources(skill_name)
    if fallback_resources:
        logger.info(f"Using fast fallback resources for {skill_name}")
        all_resources.extend(fallback_resources)
        # If we have enough from fallback, we'll skip additional search but still process through deduplication
        if len(all_resources) >= target_total // 2:  # Skip additional search if we have enough
            logger.info(f"Have enough resources from fallback, skipping additional search for {skill_name}")
            skip_additional_search = True
        else:
            skip_additional_search = False
    else:
        skip_additional_search = False
    
    # Step 2: QUALITY OVER SPEED - Search comprehensively for high-quality resources
    
    if not skip_additional_search and len(all_resources) < target_total:
        logger.info(f"Comprehensive search for QUALITY resources for {skill_name}")
        
        # Comprehensive search terms for maximum quality and variety
        search_terms = [
            f"{skill_name} complete guide",
            f"{skill_name} tutorial",
            f"{skill_name} documentation", 
            f"{skill_name} examples",
            f"{skill_name} masterclass",
            f"{skill_name} course",
            f"{skill_name} best practices"
        ]
        
        # Prioritize resource types we don't have enough of
        current_type_counts = {}
        for resource in all_resources:
            rtype = resource.get('resource_type', 'unknown')
            current_type_counts[rtype] = current_type_counts.get(rtype, 0) + 1
        
        # Order resource types by priority (least represented first)
        type_priority = sorted(resource_types, key=lambda t: current_type_counts.get(t, 0))
        
        # Search for each resource type with focus on diversity and quality
        for resource_type in type_priority:
            current_count = current_type_counts.get(resource_type, 0)
            if current_count >= max_per_type * 2:  # Allow more resources for quality filtering
                continue
                
            type_resources = []
            needed = (max_per_type * 2) - current_count  # Fetch extra for quality filtering
            
            # Try multiple search terms for comprehensive coverage
            for search_term in search_terms[:4]:  # Use more search terms for quality
                if len(type_resources) >= needed:
                    break
                    
                try:
                    if resource_type == 'video':
                        results = get_youtube_videos(search_term, max(3, needed//2))
                    elif resource_type == 'article':
                        results = get_articles(search_term, max(3, needed//2))
                    elif resource_type == 'github':
                        results = get_github_repos(search_term, max(3, needed//2))
                    elif resource_type == 'documentation':
                        # Search for documentation specifically
                        doc_search = f"{search_term} documentation official"
                        results = get_articles(doc_search, max(3, needed//2))
                        # Mark as documentation type
                        for r in results:
                            if 'docs.' in r['url'] or '/doc' in r['url'] or 'documentation' in r['title'].lower():
                                r['resource_type'] = 'documentation'
                                r['quality_score'] = r.get('quality_score', 70) + 10  # Bonus for docs
                    elif resource_type == 'tutorial':
                        # Search for tutorials specifically  
                        tutorial_search = f"{search_term} step by step complete"
                        results = get_articles(tutorial_search, max(3, needed//2))
                        # Mark as tutorial type
                        for r in results:
                            if 'tutorial' in r['title'].lower() or 'step' in r['title'].lower():
                                r['resource_type'] = 'tutorial'
                                r['quality_score'] = r.get('quality_score', 70) + 5  # Bonus for tutorials
                    elif resource_type == 'course':
                        # Search for courses specifically
                        course_search = f"{search_term} course complete training"
                        results = get_articles(course_search, max(3, needed//2))
                        # Mark as course type
                        for r in results:
                            if any(word in r['title'].lower() for word in ['course', 'training', 'bootcamp', 'certification']):
                                r['resource_type'] = 'course'
                                r['quality_score'] = r.get('quality_score', 70) + 8  # Bonus for courses
                    else:
                        continue
                    
                    # Filter out duplicates and add to type_resources
                    existing_urls = {r['url'] for r in all_resources + type_resources}
                    for result in results:
                        if result['url'] not in existing_urls and len(type_resources) < needed:
                            type_resources.append(result)
                            existing_urls.add(result['url'])
                            
                except Exception as e:
                    logger.error(f"Error searching for {resource_type} resources: {e}")
                    continue
            
            # Sort type_resources by quality score and take the best ones
            type_resources.sort(key=lambda x: x.get('quality_score', 0), reverse=True)
            all_resources.extend(type_resources[:max_per_type])
            
            # Add small delay only between different resource types, not queries
            time.sleep(0.1)
    
    # Step 3: Sort all resources by quality score and return the best ones
    all_resources.sort(key=lambda x: x.get('quality_score', 0), reverse=True)
    
    # Remove duplicates based on URL while preserving order
    seen_urls = set()
    unique_resources = []
    for resource in all_resources:
        url = resource.get('url', '')
        if url not in seen_urls:
            seen_urls.add(url)
            unique_resources.append(resource)
    
    all_resources = unique_resources
    
    # Ensure we have a good mix of resource types
    final_resources = []
    type_counts = {}
    
    for resource in all_resources:
        resource_type = resource.get('resource_type', 'unknown')
        if type_counts.get(resource_type, 0) < max_per_type:
            final_resources.append(resource)
            type_counts[resource_type] = type_counts.get(resource_type, 0) + 1
            
            if len(final_resources) >= target_total:
                break
    # If we don't have enough resources, use robust fetcher as additional fallback
    if len(final_resources) < target_total // 2:
        logger.info(f"Using robust fetcher as fallback for {skill_name}")
        try:
            robust_resources = get_robust_resources(skill_name, resource_types, max_per_type=3)
            if robust_resources:
                final_resources.extend(robust_resources)
                logger.info(f"Added {len(robust_resources)} resources from robust fetcher")
        except Exception as e:
            logger.error(f"Robust fetcher failed for {skill_name}: {e}")
    
    # If we still don't have enough resources, use fast fallback
    if len(final_resources) < 2:
        logger.info(f"Using fast fallback resources for {skill_name}")
        fallback_resources = get_fast_fallback_resources(skill_name)
        if fallback_resources:
            final_resources.extend(fallback_resources)
    
    # Final step: Apply enhanced uniqueness and quality filtering to all resources
    final_resources = ensure_resource_uniqueness_and_quality(all_resources, skill_name, target_total)
    
    # Cache the results for future requests
    cache_resources(cache_key, final_resources)
    
    logger.info(f"Returning {len(final_resources)} unique, high-quality resources for {skill_name}")
    return final_resources

def get_default_resources(skill_name):
    """
    Get a list of default resources for a skill in case dynamic search fails.
    
    Args:
        skill_name (str): Name of the skill
        
    Returns:
        list: List of default resource dictionaries
    """
    default_resources = [
        {
            'title': f"{skill_name} Tutorial for Beginners",
            'url': "https://www.freecodecamp.org/",
            'description': f"A comprehensive guide to learning {skill_name}",
            'resource_type': 'article'
        },
        {
            'title': f"Introduction to {skill_name}",
            'url': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            'description': f"Video tutorial introduction to {skill_name}",
            'resource_type': 'video'
        },
        {
            'title': f"{skill_name} Examples Repository",
            'url': "https://github.com/topics/learning-resources",
            'description': f"GitHub repository with {skill_name} examples and exercises",
            'resource_type': 'github'
        }
    ]
    
    return default_resources