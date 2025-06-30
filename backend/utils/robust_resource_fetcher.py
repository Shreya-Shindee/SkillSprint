"""
Robust resource fetcher with multiple fallback mechanisms to handle API rate limiting.
This system ensures we always get comprehensive, high-quality resources for each subskill.
"""
import requests
from bs4 import BeautifulSoup
import random
import time
import logging
from urllib.parse import quote_plus
import json

logger = logging.getLogger(__name__)

class RobustResourceFetcher:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
        
        # Rate limiting
        self.last_request_time = {}
        self.min_delay = 1.5  # Minimum delay between requests to same service
        
        # Backup resource databases for when APIs fail
        self.backup_resources = self._initialize_backup_resources()
        
    def _initialize_backup_resources(self):
        """Initialize comprehensive backup resources for all subskills."""
        return {
            # Programming Fundamentals
            "Arrays": [
                {"title": "Complete Array Tutorial - GeeksforGeeks", "url": "https://www.geeksforgeeks.org/array-data-structure/", "type": "article", "score": 95},
                {"title": "Array Problems Practice - LeetCode", "url": "https://leetcode.com/tag/array/", "type": "course", "score": 92},
                {"title": "Array Algorithms Documentation", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array", "type": "documentation", "score": 94},
                {"title": "Array Data Structures Video Course", "url": "https://www.youtube.com/watch?v=QJNwK2uJyGs", "type": "video", "score": 88},
                {"title": "Python Array Implementations", "url": "https://github.com/TheAlgorithms/Python/tree/master/data_structures/arrays", "type": "github", "score": 86},
                {"title": "Interactive Array Tutorial", "url": "https://www.programiz.com/dsa/array", "type": "tutorial", "score": 85},
                {"title": "Array Rotation Techniques", "url": "https://www.geeksforgeeks.org/array-rotation/", "type": "article", "score": 90},
                {"title": "Advanced Array Patterns", "url": "https://leetcode.com/discuss/study-guide/1152328/Arrays-study-guide", "type": "course", "score": 89}
            ],
            "Linked Lists": [
                {"title": "Linked List Comprehensive Guide", "url": "https://www.geeksforgeeks.org/data-structures/linked-list/", "type": "article", "score": 95},
                {"title": "Linked List Problems - LeetCode", "url": "https://leetcode.com/tag/linked-list/", "type": "course", "score": 91},
                {"title": "CS50 Linked Lists Documentation", "url": "https://cs50.harvard.edu/x/2023/notes/5/", "type": "documentation", "score": 93},
                {"title": "Linked List Masterclass Video", "url": "https://www.youtube.com/watch?v=WwfhLC16bis", "type": "video", "score": 87},
                {"title": "Linked List Implementations Repository", "url": "https://github.com/TheAlgorithms/Python/tree/master/data_structures/linked_list", "type": "github", "score": 85},
                {"title": "Interactive Linked List Visualization", "url": "https://www.cs.usfca.edu/~galles/visualization/LinkedList.html", "type": "tutorial", "score": 89},
                {"title": "Reverse Linked List Patterns", "url": "https://www.geeksforgeeks.org/reverse-a-linked-list/", "type": "article", "score": 88},
                {"title": "Advanced Linked List Course", "url": "https://leetcode.com/explore/learn/card/linked-list/", "type": "course", "score": 90}
            ],
            "Binary Trees": [
                {"title": "Binary Tree Complete Tutorial", "url": "https://www.geeksforgeeks.org/binary-tree-data-structure/", "type": "article", "score": 94},
                {"title": "Tree Traversal Algorithms", "url": "https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/", "type": "article", "score": 92},
                {"title": "Binary Tree Problems - LeetCode", "url": "https://leetcode.com/tag/binary-tree/", "type": "course", "score": 90},
                {"title": "Tree Data Structures Documentation", "url": "https://en.wikipedia.org/wiki/Binary_tree", "type": "documentation", "score": 88},
                {"title": "Binary Tree Video Tutorial", "url": "https://www.youtube.com/watch?v=H5JubkIy_p8", "type": "video", "score": 86},
                {"title": "Tree Algorithms Repository", "url": "https://github.com/TheAlgorithms/Python/tree/master/data_structures/binary_tree", "type": "github", "score": 84},
                {"title": "Interactive Tree Visualization", "url": "https://www.cs.usfca.edu/~galles/visualization/BST.html", "type": "tutorial", "score": 87},
                {"title": "Advanced Tree Patterns Course", "url": "https://leetcode.com/explore/learn/card/data-structure-tree/", "type": "course", "score": 89}
            ],
            "Dynamic Programming": [
                {"title": "Dynamic Programming Masterclass", "url": "https://www.geeksforgeeks.org/dynamic-programming/", "type": "article", "score": 95},
                {"title": "DP Pattern Recognition Guide", "url": "https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns", "type": "article", "score": 93},
                {"title": "Dynamic Programming Problems", "url": "https://leetcode.com/tag/dynamic-programming/", "type": "course", "score": 91},
                {"title": "DP Algorithms Documentation", "url": "https://en.wikipedia.org/wiki/Dynamic_programming", "type": "documentation", "score": 87},
                {"title": "DP Tutorial Video Series", "url": "https://www.youtube.com/watch?v=oBt53YbR9Kk", "type": "video", "score": 89},
                {"title": "DP Implementations Repository", "url": "https://github.com/TheAlgorithms/Python/tree/master/dynamic_programming", "type": "github", "score": 85},
                {"title": "Interactive DP Tutorial", "url": "https://www.programiz.com/dsa/dynamic-programming", "type": "tutorial", "score": 86},
                {"title": "Advanced DP Techniques Course", "url": "https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews", "type": "course", "score": 92}
            ],
            "Sorting Algorithms": [
                {"title": "Sorting Algorithms Complete Guide", "url": "https://www.geeksforgeeks.org/sorting-algorithms/", "type": "article", "score": 94},
                {"title": "Sorting Algorithm Comparisons", "url": "https://www.geeksforgeeks.org/analysis-of-different-sorting-techniques/", "type": "article", "score": 91},
                {"title": "Sorting Problems Practice", "url": "https://leetcode.com/tag/sorting/", "type": "course", "score": 88},
                {"title": "Sorting Algorithms Documentation", "url": "https://en.wikipedia.org/wiki/Sorting_algorithm", "type": "documentation", "score": 86},
                {"title": "Sorting Algorithms Video Tutorial", "url": "https://www.youtube.com/watch?v=kPRA0W1kECg", "type": "video", "score": 87},
                {"title": "Sorting Implementations Repository", "url": "https://github.com/TheAlgorithms/Python/tree/master/sorts", "type": "github", "score": 84},
                {"title": "Interactive Sorting Visualization", "url": "https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html", "type": "tutorial", "score": 89},
                {"title": "Advanced Sorting Techniques", "url": "https://www.programiz.com/dsa/sorting-algorithm", "type": "tutorial", "score": 85}
            ],
            "Searching Algorithms": [
                {"title": "Searching Algorithms Tutorial", "url": "https://www.geeksforgeeks.org/searching-algorithms/", "type": "article", "score": 93},
                {"title": "Binary Search Masterclass", "url": "https://www.geeksforgeeks.org/binary-search/", "type": "article", "score": 92},
                {"title": "Search Problems - LeetCode", "url": "https://leetcode.com/tag/binary-search/", "type": "course", "score": 89},
                {"title": "Search Algorithms Documentation", "url": "https://en.wikipedia.org/wiki/Search_algorithm", "type": "documentation", "score": 85},
                {"title": "Search Algorithms Video Course", "url": "https://www.youtube.com/watch?v=MFhxShGxHWc", "type": "video", "score": 86},
                {"title": "Search Implementations Repository", "url": "https://github.com/TheAlgorithms/Python/tree/master/searches", "type": "github", "score": 83},
                {"title": "Interactive Search Tutorial", "url": "https://www.cs.usfca.edu/~galles/visualization/Search.html", "type": "tutorial", "score": 87},
                {"title": "Advanced Search Patterns", "url": "https://leetcode.com/discuss/study-guide/786126/Python-Powerful-Ultimate-Binary-Search-Template", "type": "course", "score": 90}
            ],
            
            # Web Development
            "HTML Fundamentals": [
                {"title": "HTML Complete Reference - MDN", "url": "https://developer.mozilla.org/en-US/docs/Web/HTML", "type": "documentation", "score": 98},
                {"title": "HTML Tutorial - W3Schools", "url": "https://www.w3schools.com/html/", "type": "tutorial", "score": 90},
                {"title": "HTML Crash Course Video", "url": "https://www.youtube.com/watch?v=UB1O30fR-EE", "type": "video", "score": 87},
                {"title": "HTML5 Semantic Elements Guide", "url": "https://www.w3schools.com/html/html5_semantic_elements.asp", "type": "article", "score": 89},
                {"title": "HTML Forms Complete Guide", "url": "https://developer.mozilla.org/en-US/docs/Learn/Forms", "type": "documentation", "score": 92},
                {"title": "Interactive HTML Course", "url": "https://www.freecodecamp.org/learn/responsive-web-design/", "type": "course", "score": 94},
                {"title": "HTML Best Practices", "url": "https://github.com/hail2u/html-best-practices", "type": "github", "score": 85},
                {"title": "Accessibility in HTML", "url": "https://webaim.org/intro/", "type": "article", "score": 88}
            ],
            "CSS Fundamentals": [
                {"title": "CSS Complete Reference - MDN", "url": "https://developer.mozilla.org/en-US/docs/Web/CSS", "type": "documentation", "score": 98},
                {"title": "CSS Tutorial - W3Schools", "url": "https://www.w3schools.com/css/", "type": "tutorial", "score": 90},
                {"title": "CSS Flexbox Complete Guide", "url": "https://css-tricks.com/snippets/css/a-guide-to-flexbox/", "type": "article", "score": 95},
                {"title": "CSS Grid Layout Tutorial", "url": "https://css-tricks.com/snippets/css/complete-guide-grid/", "type": "article", "score": 94},
                {"title": "CSS Video Course", "url": "https://www.youtube.com/watch?v=1Rs2ND1ryYc", "type": "video", "score": 88},
                {"title": "CSS Animations Tutorial", "url": "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations", "type": "documentation", "score": 91},
                {"title": "CSS Games for Learning", "url": "https://github.com/AllThingsSmitty/css-protips", "type": "github", "score": 86},
                {"title": "Interactive CSS Course", "url": "https://www.freecodecamp.org/learn/responsive-web-design/", "type": "course", "score": 92}
            ],
            "JavaScript Fundamentals": [
                {"title": "JavaScript Complete Guide - MDN", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript", "type": "documentation", "score": 98},
                {"title": "JavaScript.info - Modern Tutorial", "url": "https://javascript.info/", "type": "tutorial", "score": 96},
                {"title": "JavaScript Crash Course Video", "url": "https://www.youtube.com/watch?v=hdI2bqOjy3c", "type": "video", "score": 89},
                {"title": "JavaScript ES6+ Features", "url": "https://github.com/lukehoban/es6features", "type": "github", "score": 87},
                {"title": "You Don't Know JS Book Series", "url": "https://github.com/getify/You-Dont-Know-JS", "type": "github", "score": 94},
                {"title": "JavaScript Algorithms Practice", "url": "https://github.com/trekhleb/javascript-algorithms", "type": "github", "score": 91},
                {"title": "Interactive JavaScript Course", "url": "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/", "type": "course", "score": 93},
                {"title": "JavaScript Design Patterns", "url": "https://addyosmani.com/resources/essentialjsdesignpatterns/book/", "type": "article", "score": 88}
            ],
            "React Fundamentals": [
                {"title": "React Official Documentation", "url": "https://react.dev/", "type": "documentation", "score": 98},
                {"title": "React Tutorial - Official", "url": "https://react.dev/learn", "type": "tutorial", "score": 95},
                {"title": "React Crash Course Video", "url": "https://www.youtube.com/watch?v=w7ejDZ8SWv8", "type": "video", "score": 89},
                {"title": "React Hooks Complete Guide", "url": "https://react.dev/reference/react", "type": "documentation", "score": 93},
                {"title": "React Patterns and Best Practices", "url": "https://github.com/vasanthk/react-bits", "type": "github", "score": 87},
                {"title": "React Router Tutorial", "url": "https://reactrouter.com/en/main/start/tutorial", "type": "tutorial", "score": 90},
                {"title": "Interactive React Course", "url": "https://scrimba.com/learn/learnreact", "type": "course", "score": 91},
                {"title": "React Testing Best Practices", "url": "https://kentcdodds.com/blog/common-mistakes-with-react-testing-library", "type": "article", "score": 86}
            ],
            "Node.js Backend": [
                {"title": "Node.js Official Documentation", "url": "https://nodejs.org/en/docs/", "type": "documentation", "score": 97},
                {"title": "Node.js Tutorial - W3Schools", "url": "https://www.w3schools.com/nodejs/", "type": "tutorial", "score": 88},
                {"title": "Node.js Crash Course Video", "url": "https://www.youtube.com/watch?v=fBNz5xF-Kx4", "type": "video", "score": 87},
                {"title": "Express.js Official Guide", "url": "https://expressjs.com/en/guide/routing.html", "type": "documentation", "score": 94},
                {"title": "Node.js Best Practices", "url": "https://github.com/goldbergyoni/nodebestpractices", "type": "github", "score": 92},
                {"title": "RESTful API with Node.js", "url": "https://restfulapi.net/", "type": "article", "score": 89},
                {"title": "Node.js Authentication Tutorial", "url": "https://www.digitalocean.com/community/tutorials/api-authentication-with-json-web-tokens-jwt-and-passport", "type": "tutorial", "score": 85},
                {"title": "Node.js Performance Best Practices", "url": "https://nodejs.org/en/docs/guides/simple-profiling/", "type": "documentation", "score": 90}
            ],
            
            # Machine Learning
            "Linear Algebra for ML": [
                {"title": "Linear Algebra for Machine Learning", "url": "https://machinelearningmastery.com/linear-algebra-machine-learning/", "type": "article", "score": 93},
                {"title": "Khan Academy Linear Algebra", "url": "https://www.khanacademy.org/math/linear-algebra", "type": "course", "score": 95},
                {"title": "3Blue1Brown Linear Algebra Series", "url": "https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab", "type": "video", "score": 97},
                {"title": "NumPy Linear Algebra Documentation", "url": "https://numpy.org/doc/stable/reference/routines.linalg.html", "type": "documentation", "score": 89},
                {"title": "Linear Algebra Implementations", "url": "https://github.com/fastai/numerical-linear-algebra", "type": "github", "score": 87},
                {"title": "Interactive Linear Algebra", "url": "http://immersivemath.com/ila/index.html", "type": "tutorial", "score": 91},
                {"title": "MIT Linear Algebra Course", "url": "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/", "type": "course", "score": 96},
                {"title": "Linear Algebra Cheat Sheet", "url": "https://towardsdatascience.com/linear-algebra-cheat-sheet-for-deep-learning-cd67aba4526c", "type": "article", "score": 84}
            ],
            "Statistics for ML": [
                {"title": "Statistics for Machine Learning", "url": "https://machinelearningmastery.com/statistics_for_machine_learning/", "type": "article", "score": 92},
                {"title": "Khan Academy Statistics", "url": "https://www.khanacademy.org/math/statistics-probability", "type": "course", "score": 94},
                {"title": "StatQuest Video Series", "url": "https://www.youtube.com/user/joshstarmer", "type": "video", "score": 96},
                {"title": "SciPy Statistics Documentation", "url": "https://docs.scipy.org/doc/scipy/reference/stats.html", "type": "documentation", "score": 88},
                {"title": "Statistics with Python", "url": "https://github.com/rouseguy/intro2stats", "type": "github", "score": 85},
                {"title": "Interactive Statistics Course", "url": "https://seeing-theory.brown.edu/", "type": "tutorial", "score": 93},
                {"title": "MIT Statistics Course", "url": "https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2014/", "type": "course", "score": 95},
                {"title": "Bayesian Statistics Tutorial", "url": "https://towardsdatascience.com/a-gentle-introduction-to-bayesian-deep-learning-d298c7243fd6", "type": "article", "score": 87}
            ],
            "Supervised Learning": [
                {"title": "Supervised Learning Complete Guide", "url": "https://machinelearningmastery.com/supervised-and-unsupervised-machine-learning-algorithms/", "type": "article", "score": 91},
                {"title": "Scikit-learn User Guide", "url": "https://scikit-learn.org/stable/user_guide.html", "type": "documentation", "score": 96},
                {"title": "Machine Learning Course - Andrew Ng", "url": "https://www.coursera.org/learn/machine-learning", "type": "course", "score": 98},
                {"title": "ML Algorithms Video Explanations", "url": "https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF", "type": "video", "score": 89},
                {"title": "ML Algorithms from Scratch", "url": "https://github.com/eriklindernoren/ML-From-Scratch", "type": "github", "score": 87},
                {"title": "Interactive ML Course", "url": "https://www.kaggle.com/learn/intro-to-machine-learning", "type": "course", "score": 92},
                {"title": "Hands-On Machine Learning Book", "url": "https://github.com/ageron/handson-ml2", "type": "github", "score": 94},
                {"title": "ML Model Evaluation Tutorial", "url": "https://machinelearningmastery.com/metrics-evaluate-machine-learning-algorithms-python/", "type": "tutorial", "score": 86}
            ],
            "Deep Learning": [
                {"title": "Deep Learning Specialization", "url": "https://www.coursera.org/specializations/deep-learning", "type": "course", "score": 98},
                {"title": "Deep Learning Book - Ian Goodfellow", "url": "https://www.deeplearningbook.org/", "type": "documentation", "score": 97},
                {"title": "TensorFlow Official Tutorials", "url": "https://www.tensorflow.org/tutorials", "type": "tutorial", "score": 95},
                {"title": "PyTorch Tutorials", "url": "https://pytorch.org/tutorials/", "type": "tutorial", "score": 94},
                {"title": "3Blue1Brown Neural Networks", "url": "https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi", "type": "video", "score": 96},
                {"title": "Deep Learning Papers Repository", "url": "https://github.com/floodsung/Deep-Learning-Papers-Reading-Roadmap", "type": "github", "score": 89},
                {"title": "Fast.ai Deep Learning Course", "url": "https://course.fast.ai/", "type": "course", "score": 93},
                {"title": "Deep Learning Fundamentals", "url": "https://towardsdatascience.com/deep-learning-fundamentals-handbook-theoretical-and-practical-aspects-a35b7d1b5c5e", "type": "article", "score": 87}
            ],
            
            # Python
            "Python Basics": [
                {"title": "Python Official Tutorial", "url": "https://docs.python.org/3/tutorial/", "type": "documentation", "score": 97},
                {"title": "Python for Beginners - Microsoft", "url": "https://docs.microsoft.com/en-us/learn/paths/beginner-python/", "type": "course", "score": 93},
                {"title": "Python Crash Course Video", "url": "https://www.youtube.com/watch?v=rfscVS0vtbw", "type": "video", "score": 89},
                {"title": "Real Python Tutorials", "url": "https://realpython.com/", "type": "tutorial", "score": 95},
                {"title": "Python Tricks Book Repository", "url": "https://github.com/realpython/python-tricks-the-book", "type": "github", "score": 88},
                {"title": "Interactive Python Course", "url": "https://www.codecademy.com/learn/learn-python-3", "type": "course", "score": 91},
                {"title": "Python Style Guide (PEP 8)", "url": "https://pep8.org/", "type": "documentation", "score": 86},
                {"title": "Automate the Boring Stuff", "url": "https://automatetheboringstuff.com/", "type": "tutorial", "score": 92}
            ],
            "Object-Oriented Programming": [
                {"title": "Python OOP Complete Guide", "url": "https://realpython.com/python3-object-oriented-programming/", "type": "article", "score": 94},
                {"title": "OOP Concepts Tutorial", "url": "https://www.programiz.com/python-programming/object-oriented-programming", "type": "tutorial", "score": 89},
                {"title": "Python OOP Video Course", "url": "https://www.youtube.com/watch?v=ZDa-Z5JzLYM", "type": "video", "score": 87},
                {"title": "Python Classes Documentation", "url": "https://docs.python.org/3/tutorial/classes.html", "type": "documentation", "score": 95},
                {"title": "OOP Design Patterns in Python", "url": "https://github.com/faif/python-patterns", "type": "github", "score": 91},
                {"title": "Interactive OOP Course", "url": "https://www.codecademy.com/learn/learn-python-3", "type": "course", "score": 88},
                {"title": "SOLID Principles in Python", "url": "https://realpython.com/solid-principles-python/", "type": "article", "score": 92},
                {"title": "Python OOP Best Practices", "url": "https://realpython.com/inheritance-composition-python/", "type": "tutorial", "score": 86}
            ],
            "Python Libraries": [
                {"title": "NumPy Documentation", "url": "https://numpy.org/doc/stable/", "type": "documentation", "score": 96},
                {"title": "Pandas User Guide", "url": "https://pandas.pydata.org/docs/user_guide/", "type": "documentation", "score": 95},
                {"title": "Matplotlib Tutorials", "url": "https://matplotlib.org/stable/tutorials/index.html", "type": "tutorial", "score": 93},
                {"title": "Python Data Science Handbook", "url": "https://jakevdp.github.io/PythonDataScienceHandbook/", "type": "tutorial", "score": 97},
                {"title": "Scientific Python Video Course", "url": "https://www.youtube.com/playlist?list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF", "type": "video", "score": 88},
                {"title": "Awesome Python Libraries", "url": "https://github.com/vinta/awesome-python", "type": "github", "score": 90},
                {"title": "Data Analysis with Python", "url": "https://www.freecodecamp.org/learn/data-analysis-with-python/", "type": "course", "score": 92},
                {"title": "Seaborn Statistical Visualization", "url": "https://seaborn.pydata.org/tutorial.html", "type": "tutorial", "score": 89}
            ]
        }
    
    def _wait_for_rate_limit(self, service):
        """Implement rate limiting to avoid API blocks."""
        current_time = time.time()
        if service in self.last_request_time:
            time_since_last = current_time - self.last_request_time[service]
            if time_since_last < self.min_delay:
                sleep_time = self.min_delay - time_since_last
                logger.info(f"Rate limiting: waiting {sleep_time:.2f}s for {service}")
                time.sleep(sleep_time)
        
        self.last_request_time[service] = time.time()
    
    def search_with_fallback(self, query, resource_type, max_results=5):
        """
        Search for resources with multiple fallback mechanisms.
        
        Args:
            query (str): Search query
            resource_type (str): Type of resource (article, video, course, etc.)
            max_results (int): Maximum results to return
            
        Returns:
            list: List of resources
        """
        resources = []
        
        # Try different search engines with fallbacks
        search_methods = [
            self._search_bing,
            self._search_startpage,
            self._search_searx,
            self._get_backup_resources
        ]
        
        for method in search_methods:
            try:
                self._wait_for_rate_limit(method.__name__)
                method_resources = method(query, resource_type, max_results - len(resources))
                if method_resources:
                    resources.extend(method_resources)
                    logger.info(f"Got {len(method_resources)} resources from {method.__name__}")
                    
                if len(resources) >= max_results:
                    break
                    
            except Exception as e:
                logger.warning(f"Search method {method.__name__} failed: {e}")
                continue
        
        return resources[:max_results]
    
    def _search_bing(self, query, resource_type, max_results):
        """Search using Bing (more permissive than Google)."""
        try:
            search_query = quote_plus(f"{query} {resource_type}")
            url = f"https://www.bing.com/search?q={search_query}"
            
            response = self.session.get(url, timeout=5)
            if response.status_code != 200:
                return []
            
            soup = BeautifulSoup(response.text, 'html.parser')
            results = []
            
            # Parse Bing results
            for result in soup.find_all('li', class_='b_algo')[:max_results]:
                title_elem = result.find('h2')
                if title_elem and title_elem.find('a'):
                    link = title_elem.find('a')
                    title = link.get_text().strip()
                    url = link.get('href')
                    
                    desc_elem = result.find('p')
                    description = desc_elem.get_text().strip() if desc_elem else f"{resource_type} about {query}"
                    
                    results.append({
                        'title': title,
                        'url': url,
                        'description': description,
                        'resource_type': resource_type,
                        'quality_score': 75
                    })
            
            return results
            
        except Exception as e:
            logger.error(f"Bing search failed: {e}")
            return []
    
    def _search_startpage(self, query, resource_type, max_results):
        """Search using Startpage (privacy-focused)."""
        try:
            search_query = quote_plus(f"{query} {resource_type}")
            url = f"https://www.startpage.com/sp/search?q={search_query}"
            
            response = self.session.get(url, timeout=5)
            if response.status_code != 200:
                return []
            
            soup = BeautifulSoup(response.text, 'html.parser')
            results = []
            
            # Parse Startpage results
            for result in soup.find_all('div', class_='w-gl__result')[:max_results]:
                title_elem = result.find('h3')
                if title_elem and title_elem.find('a'):
                    link = title_elem.find('a')
                    title = link.get_text().strip()
                    url = link.get('href')
                    
                    desc_elem = result.find('p', class_='w-gl__description')
                    description = desc_elem.get_text().strip() if desc_elem else f"{resource_type} about {query}"
                    
                    results.append({
                        'title': title,
                        'url': url,
                        'description': description,
                        'resource_type': resource_type,
                        'quality_score': 78
                    })
            
            return results
            
        except Exception as e:
            logger.error(f"Startpage search failed: {e}")
            return []
    
    def _search_searx(self, query, resource_type, max_results):
        """Search using SearX instances (open source meta-search)."""
        # Public SearX instances
        searx_instances = [
            "https://searx.be",
            "https://search.privacyguides.net",
            "https://searx.tiekoetter.com"
        ]
        
        for instance in searx_instances:
            try:
                search_query = quote_plus(f"{query} {resource_type}")
                url = f"{instance}/search?q={search_query}&format=json"
                
                response = self.session.get(url, timeout=5)
                if response.status_code != 200:
                    continue
                
                data = response.json()
                results = []
                
                for result in data.get('results', [])[:max_results]:
                    results.append({
                        'title': result.get('title', ''),
                        'url': result.get('url', ''),
                        'description': result.get('content', f"{resource_type} about {query}"),
                        'resource_type': resource_type,
                        'quality_score': 72
                    })
                
                if results:
                    return results
                    
            except Exception as e:
                logger.error(f"SearX search failed for {instance}: {e}")
                continue
        
        return []
    
    def _get_backup_resources(self, query, resource_type, max_results):
        """Get resources from backup database when all searches fail."""
        query_lower = query.lower()
        
        # Find matching subskill
        for subskill, resources in self.backup_resources.items():
            if (subskill.lower() in query_lower or 
                any(word in query_lower for word in subskill.lower().split())):
                
                # Filter by resource type if specified
                if resource_type != 'all':
                    filtered_resources = [r for r in resources if r.get('type') == resource_type]
                else:
                    filtered_resources = resources
                
                # Convert to expected format
                converted_resources = []
                for resource in filtered_resources[:max_results]:
                    converted_resources.append({
                        'title': resource['title'],
                        'url': resource['url'],
                        'description': f"High-quality {resource.get('type', 'resource')} for {subskill}",
                        'resource_type': resource.get('type', resource_type),
                        'quality_score': resource.get('score', 85)
                    })
                
                return converted_resources
        
        return []

# Global instance
robust_fetcher = RobustResourceFetcher()

def get_robust_resources(skill_name, resource_types=None, max_per_type=8):
    """
    Get comprehensive resources using the robust fetcher.
    
    Args:
        skill_name (str): Name of the skill/subskill
        resource_types (list): Types of resources to fetch
        max_per_type (int): Maximum resources per type
        
    Returns:
        list: Comprehensive list of resources
    """
    if resource_types is None:
        resource_types = ['article', 'video', 'course', 'documentation', 'tutorial', 'github']
    
    all_resources = []
    
    for resource_type in resource_types:
        logger.info(f"Fetching {resource_type} resources for {skill_name}")
        resources = robust_fetcher.search_with_fallback(skill_name, resource_type, max_per_type)
        all_resources.extend(resources)
    
    # Remove duplicates and sort by quality
    seen_urls = set()
    unique_resources = []
    
    for resource in sorted(all_resources, key=lambda x: x.get('quality_score', 50), reverse=True):
        if resource['url'] not in seen_urls:
            seen_urls.add(resource['url'])
            unique_resources.append(resource)
    
    logger.info(f"Total robust resources for {skill_name}: {len(unique_resources)}")
    return unique_resources
