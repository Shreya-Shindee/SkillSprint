"""
Fast fallback resources for common skills to avoid API timeouts.
Now includes comprehensive subskill-specific resources for detailed learning paths.
"""

# Enhanced fast fallback resources with subskill specificity
FAST_FALLBACK_RESOURCES = {
    # === DSA SUBSKILLS - UNIQUE RESOURCES FOR EACH ===
    "Arrays": [
        {
            "title": "Array Data Structure Complete Guide",
            "url": "https://www.geeksforgeeks.org/array-data-structure/",
            "description": "Comprehensive array tutorial with problems and solutions",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Array Problems - LeetCode",
            "url": "https://leetcode.com/tag/array/",
            "description": "Practice array problems with detailed explanations",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "Array Algorithms Visualization",
            "url": "https://www.cs.usfca.edu/~galles/visualization/Array.html",
            "description": "Interactive visualization of array operations",
            "resource_type": "article",
            "quality_score": 88
        },
        {
            "title": "Two Pointer Technique for Arrays",
            "url": "https://www.geeksforgeeks.org/two-pointers-technique/",
            "description": "Master the two-pointer technique for array problems",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "Linked Lists": [
        {
            "title": "Linked List Complete Tutorial",
            "url": "https://www.geeksforgeeks.org/data-structures/linked-list/",
            "description": "Complete guide to linked lists with implementations",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Linked List Visualization",
            "url": "https://www.cs.usfca.edu/~galles/visualization/LinkedList.html",
            "description": "Interactive linked list operations visualization",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "Linked List Problems - LeetCode",
            "url": "https://leetcode.com/tag/linked-list/",
            "description": "Practice linked list problems with step-by-step solutions",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "Fast and Slow Pointer Technique",
            "url": "https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/",
            "description": "Learn cycle detection and other linked list patterns",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "Binary Trees": [
        {
            "title": "Binary Tree Complete Guide",
            "url": "https://www.geeksforgeeks.org/binary-tree-data-structure/",
            "description": "Comprehensive binary tree tutorial with traversals",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Tree Traversal Visualization",
            "url": "https://www.cs.usfca.edu/~galles/visualization/BinTree.html",
            "description": "Interactive binary tree traversal visualization",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "Binary Tree Problems - LeetCode",
            "url": "https://leetcode.com/tag/tree/",
            "description": "Practice tree problems with detailed explanations",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "Tree Algorithms Patterns",
            "url": "https://www.geeksforgeeks.org/binary-tree-set-1-introduction/",
            "description": "Common patterns and techniques for tree problems",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "Binary Search Trees": [
        {
            "title": "BST Complete Tutorial",
            "url": "https://www.geeksforgeeks.org/binary-search-tree-data-structure/",
            "description": "Complete guide to Binary Search Trees",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "BST Visualization",
            "url": "https://www.cs.usfca.edu/~galles/visualization/BST.html",
            "description": "Interactive BST operations visualization",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "BST Problems Practice",
            "url": "https://leetcode.com/tag/binary-search-tree/",
            "description": "Practice BST problems with solutions",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "AVL Trees and Self-Balancing",
            "url": "https://www.geeksforgeeks.org/avl-tree-set-1-insertion/",
            "description": "Learn about self-balancing BSTs",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "Stacks": [
        {
            "title": "Stack Data Structure Guide",
            "url": "https://www.geeksforgeeks.org/stack-data-structure/",
            "description": "Complete stack tutorial with applications",
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
            "title": "Stack Problems - LeetCode",
            "url": "https://leetcode.com/tag/stack/",
            "description": "Practice stack problems with explanations",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "Monotonic Stack Technique",
            "url": "https://www.geeksforgeeks.org/introduction-to-monotonic-stack/",
            "description": "Master the monotonic stack pattern",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "Queues": [
        {
            "title": "Queue Data Structure Guide",
            "url": "https://www.geeksforgeeks.org/queue-data-structure/",
            "description": "Complete queue tutorial with implementations",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Queue Visualization",
            "url": "https://www.cs.usfca.edu/~galles/visualization/QueueArray.html",
            "description": "Interactive queue operations visualization",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "Priority Queue Tutorial",
            "url": "https://www.geeksforgeeks.org/priority-queue-set-1-introduction/",
            "description": "Learn about priority queues and heaps",
            "resource_type": "article",
            "quality_score": 88
        },
        {
            "title": "Deque (Double-ended Queue)",
            "url": "https://www.geeksforgeeks.org/deque-set-1-introduction-applications/",
            "description": "Understanding deque and its applications",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "Graphs": [
        {
            "title": "Graph Data Structure Complete Guide",
            "url": "https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/",
            "description": "Comprehensive graph theory and algorithms",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Graph Algorithms Visualization",
            "url": "https://www.cs.usfca.edu/~galles/visualization/BFS.html",
            "description": "Interactive graph traversal visualization",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "Graph Problems - LeetCode",
            "url": "https://leetcode.com/tag/graph/",
            "description": "Practice graph problems with solutions",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "Graph Theory for Programmers",
            "url": "https://www.youtube.com/watch?v=LFKZLXVO-Dg",
            "description": "Complete graph theory course for coding interviews",
            "resource_type": "video",
            "quality_score": 85
        }
    ],
    "Dynamic Programming": [
        {
            "title": "Dynamic Programming Complete Guide",
            "url": "https://www.geeksforgeeks.org/dynamic-programming/",
            "description": "Master dynamic programming with patterns",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "DP Patterns for Coding Interviews",
            "url": "https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns",
            "description": "Common DP patterns and when to use them",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "Dynamic Programming - LeetCode",
            "url": "https://leetcode.com/tag/dynamic-programming/",
            "description": "Practice DP problems with detailed solutions",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "DP Optimization Techniques",
            "url": "https://www.geeksforgeeks.org/overlapping-subproblems-property/",
            "description": "Learn memoization and tabulation",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "Sorting Algorithms": [
        {
            "title": "Sorting Algorithms Complete Guide",
            "url": "https://www.geeksforgeeks.org/sorting-algorithms/",
            "description": "All sorting algorithms with complexity analysis",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Sorting Algorithms Visualization",
            "url": "https://www.sorting-algorithms.com/",
            "description": "Interactive visualization of all sorting algorithms",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "Merge Sort vs Quick Sort",
            "url": "https://www.geeksforgeeks.org/quick-sort-vs-merge-sort/",
            "description": "Detailed comparison of major sorting algorithms",
            "resource_type": "article",
            "quality_score": 88
        },
        {
            "title": "Counting Sort and Radix Sort",
            "url": "https://www.geeksforgeeks.org/counting-sort/",
            "description": "Non-comparison based sorting techniques",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "Searching Algorithms": [
        {
            "title": "Search Algorithms Complete Guide",
            "url": "https://www.geeksforgeeks.org/searching-algorithms/",
            "description": "All searching algorithms with implementations",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Binary Search Mastery",
            "url": "https://leetcode.com/explore/learn/card/binary-search/",
            "description": "Master binary search and its variations",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "Binary Search Visualization",
            "url": "https://www.cs.usfca.edu/~galles/visualization/Search.html",
            "description": "Interactive binary search visualization",
            "resource_type": "article",
            "quality_score": 88
        },
        {
            "title": "Advanced Search Techniques",
            "url": "https://www.geeksforgeeks.org/ternary-search/",
            "description": "Ternary search and other advanced techniques",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "Stacks": [
        {
            "title": "Stack Data Structure Guide",
            "url": "https://www.geeksforgeeks.org/stack-data-structure/",
            "description": "Complete stack implementation and applications",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Stack Operations Visualization",
            "url": "https://www.cs.usfca.edu/~galles/visualization/StackArray.html",
            "description": "Interactive stack operations visualization",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "Stack Applications Tutorial",
            "url": "https://www.programiz.com/dsa/stack",
            "description": "Real-world stack applications and use cases",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "Expression Evaluation with Stacks",
            "url": "https://www.geeksforgeeks.org/stack-set-2-infix-to-postfix/",
            "description": "Learn infix to postfix conversion using stacks",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "Queues": [
        {
            "title": "Queue Data Structure Tutorial",
            "url": "https://www.geeksforgeeks.org/queue-data-structure/",
            "description": "Comprehensive queue implementation guide",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Queue Visualization",
            "url": "https://www.cs.usfca.edu/~galles/visualization/QueueArray.html",
            "description": "Interactive queue operations visualization",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "Priority Queue and Heaps",
            "url": "https://www.programiz.com/dsa/priority-queue",
            "description": "Learn priority queues and heap data structure",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "Circular Queue Implementation",
            "url": "https://www.geeksforgeeks.org/circular-queue-set-1-introduction-array-implementation/",
            "description": "Master circular queue implementation",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "Trees": [
        {
            "title": "Tree Data Structure Complete Guide",
            "url": "https://www.geeksforgeeks.org/binary-tree-data-structure/",
            "description": "Comprehensive tree data structure tutorial",
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
            "description": "Master inorder, preorder, and postorder traversals",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "Binary Search Tree Operations",
            "url": "https://www.geeksforgeeks.org/binary-search-tree-data-structure/",
            "description": "Learn BST insertion, deletion, and search",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "Binary Trees": [
        {
            "title": "Binary Tree Problems and Solutions",
            "url": "https://www.geeksforgeeks.org/binary-tree-data-structure/",
            "description": "Comprehensive binary tree problem collection",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Binary Tree LeetCode Problems",
            "url": "https://leetcode.com/tag/binary-tree/",
            "description": "Practice binary tree coding problems",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "Tree Height and Depth Algorithms",
            "url": "https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/",
            "description": "Learn to calculate tree height and depth",
            "resource_type": "article",
            "quality_score": 88
        },
        {
            "title": "Lowest Common Ancestor",
            "url": "https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/",
            "description": "Master LCA algorithms for binary trees",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "Graphs": [
        {
            "title": "Graph Data Structure and Algorithms",
            "url": "https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/",
            "description": "Complete graph algorithms and implementations",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Graph Traversal Visualization",
            "url": "https://www.cs.usfca.edu/~galles/visualization/BFS.html",
            "description": "Interactive BFS and DFS visualization",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "Shortest Path Algorithms",
            "url": "https://www.programiz.com/dsa/dijkstra-algorithm",
            "description": "Learn Dijkstra's and other shortest path algorithms",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "Graph Cycle Detection",
            "url": "https://www.geeksforgeeks.org/detect-cycle-in-a-graph/",
            "description": "Detect cycles in directed and undirected graphs",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "Sorting Algorithms": [
        {
            "title": "Sorting Algorithms Complete Guide",
            "url": "https://www.geeksforgeeks.org/sorting-algorithms/",
            "description": "All sorting algorithms with time complexity analysis",
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
            "title": "Quick Sort vs Merge Sort",
            "url": "https://www.programiz.com/dsa/merge-sort",
            "description": "Compare and understand divide-and-conquer sorting",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "Heap Sort Implementation",
            "url": "https://www.geeksforgeeks.org/heap-sort/",
            "description": "Learn heap sort with heap data structure",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "Searching Algorithms": [
        {
            "title": "Searching Algorithms Guide",
            "url": "https://www.geeksforgeeks.org/searching-algorithms/",
            "description": "Binary search, linear search, and advanced techniques",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Binary Search Visualization",
            "url": "https://www.cs.usfca.edu/~galles/visualization/Search.html",
            "description": "Interactive binary search visualization",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "Binary Search Mastery",
            "url": "https://leetcode.com/explore/learn/card/binary-search/",
            "description": "Complete binary search tutorial with problems",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "Search in Rotated Arrays",
            "url": "https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/",
            "description": "Advanced binary search variations",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "Dynamic Programming": [
        {
            "title": "Dynamic Programming Complete Guide",
            "url": "https://www.geeksforgeeks.org/dynamic-programming/",
            "description": "DP patterns, memoization, and tabulation techniques",
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
            "title": "Dynamic Programming Visualization",
            "url": "https://www.cs.usfca.edu/~galles/visualization/DPFib.html",
            "description": "Interactive DP problem visualization",
            "resource_type": "article",
            "quality_score": 88
        },
        {
            "title": "Knapsack Problem Variants",
            "url": "https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/",
            "description": "Master the classic knapsack problem",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "Recursion": [
        {
            "title": "Recursion Complete Tutorial",
            "url": "https://www.geeksforgeeks.org/recursion/",
            "description": "Master recursion with examples and practice",
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
            "description": "Learn recursive thinking patterns",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "Tail Recursion Optimization",
            "url": "https://www.geeksforgeeks.org/tail-recursion/",
            "description": "Understand tail recursion and optimization",
            "resource_type": "article",
            "quality_score": 85
        }
    ],

    # === WEB DEVELOPMENT SUBSKILLS ===
    "HTML Basics": [
        {
            "title": "HTML5 Complete Tutorial - MDN",
            "url": "https://developer.mozilla.org/en-US/docs/Learn/HTML",
            "description": "Comprehensive HTML5 tutorial from Mozilla",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "HTML Tutorial - W3Schools",
            "url": "https://www.w3schools.com/html/",
            "description": "Interactive HTML tutorial with live examples",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "Semantic HTML5 Elements",
            "url": "https://www.freecodecamp.org/news/semantic-html5-elements/",
            "description": "Learn semantic HTML for better accessibility",
            "resource_type": "article",
            "quality_score": 85
        },
        {
            "title": "HTML Forms Deep Dive",
            "url": "https://developer.mozilla.org/en-US/docs/Learn/Forms",
            "description": "Master HTML forms and input validation",
            "resource_type": "documentation",
            "quality_score": 90
        }
    ],
    "CSS Styling": [
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
        },
        {
            "title": "CSS Animation Tutorial",
            "url": "https://www.w3schools.com/css/css3_animations.asp",
            "description": "Learn CSS transitions and animations",
            "resource_type": "course",
            "quality_score": 85
        }
    ],
    "JavaScript Fundamentals": [
        {
            "title": "JavaScript.info - Modern Tutorial",
            "url": "https://javascript.info/",
            "description": "The modern JavaScript tutorial covering all fundamentals",
            "resource_type": "article",
            "quality_score": 95
        },
        {
            "title": "You Don't Know JS",
            "url": "https://github.com/getify/You-Dont-Know-JS",
            "description": "Deep dive into JavaScript fundamentals",
            "resource_type": "github",
            "quality_score": 92
        },
        {
            "title": "JavaScript30",
            "url": "https://javascript30.com/",
            "description": "30 vanilla JavaScript projects in 30 days",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "ES6 Features Guide",
            "url": "https://www.w3schools.com/js/js_es6.asp",
            "description": "Learn modern JavaScript ES6+ features",
            "resource_type": "course",
            "quality_score": 85
        }
    ],
    "DOM Manipulation": [
        {
            "title": "DOM Manipulation Guide - MDN",
            "url": "https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction",
            "description": "Complete DOM manipulation tutorial",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "JavaScript DOM Tutorial",
            "url": "https://www.w3schools.com/js/js_htmldom.asp",
            "description": "Hands-on DOM manipulation examples",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "Event Handling in JavaScript",
            "url": "https://javascript.info/introduction-browser-events",
            "description": "Master JavaScript event handling",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "DOM Manipulation Projects",
            "url": "https://www.freecodecamp.org/news/dom-manipulation-htmlcollection-vs-nodelist/",
            "description": "Practical DOM manipulation techniques",
            "resource_type": "article",
            "quality_score": 85
        }
    ],

    # === PYTHON SUBSKILLS ===
    "Python Basics": [
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
            "description": "Learn Python through practical automation",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Python for Everybody",
            "url": "https://www.py4e.com/",
            "description": "Free Python course from University of Michigan",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "Python Exercises for Beginners",
            "url": "https://www.w3resource.com/python-exercises/",
            "description": "Practice Python with hands-on exercises",
            "resource_type": "course",
            "quality_score": 85
        }
    ],
    "Control Structures": [
        {
            "title": "Python Control Flow - Official Docs",
            "url": "https://docs.python.org/3/tutorial/controlflow.html",
            "description": "Official guide to Python control flow statements",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Python Loops Tutorial",
            "url": "https://www.w3schools.com/python/python_for_loops.asp",
            "description": "Master for loops, while loops, and control",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "Conditional Statements Guide",
            "url": "https://realpython.com/python-conditional-statements/",
            "description": "Master Python if/elif/else statements",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "Loop Control Exercises",
            "url": "https://pynative.com/python-if-else-and-for-loop-exercise/",
            "description": "Practice control structure problems",
            "resource_type": "course",
            "quality_score": 85
        }
    ],
    "Functions": [
        {
            "title": "Python Functions - Official Tutorial",
            "url": "https://docs.python.org/3/tutorial/controlflow.html#defining-functions",
            "description": "Official Python functions tutorial",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Python Functions Deep Dive",
            "url": "https://realpython.com/defining-your-own-python-function/",
            "description": "Comprehensive guide to Python functions",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "Lambda Functions Tutorial",
            "url": "https://www.w3schools.com/python/python_lambda.asp",
            "description": "Learn Python lambda and anonymous functions",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "Function Decorators Guide",
            "url": "https://realpython.com/primer-on-python-decorators/",
            "description": "Master Python decorators and advanced functions",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "Object Oriented Programming": [
        {
            "title": "OOP in Python - Real Python",
            "url": "https://realpython.com/python3-object-oriented-programming/",
            "description": "Comprehensive guide to OOP concepts in Python",
            "resource_type": "article",
            "quality_score": 95
        },
        {
            "title": "Python Classes and Objects",
            "url": "https://docs.python.org/3/tutorial/classes.html",
            "description": "Official Python classes tutorial",
            "resource_type": "documentation",
            "quality_score": 92
        },
        {
            "title": "OOP Tutorial - Programiz",
            "url": "https://www.programiz.com/python-programming/object-oriented-programming",
            "description": "Step-by-step OOP tutorial with examples",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "Python Design Patterns",
            "url": "https://github.com/faif/python-patterns",
            "description": "Python implementation of design patterns",
            "resource_type": "github",
            "quality_score": 85
        }
    ],

    # Continue with existing main skill resources...
    "Python": [
        {
            "title": "Python Official Tutorial",
            "url": "https://docs.python.org/3/tutorial/",
            "description": "The official Python tutorial covering all basics - completely free",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Automate the Boring Stuff with Python",
            "url": "https://automatetheboringstuff.com/",
            "description": "Free online book for practical Python programming",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Python for Beginners - freeCodeCamp",
            "url": "https://www.freecodecamp.org/learn/scientific-computing-with-python/",
            "description": "Free comprehensive Python course with certificates",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "Python Tutorial - W3Schools",
            "url": "https://www.w3schools.com/python/",
            "description": "Free interactive Python tutorial with examples",
            "resource_type": "course",
            "quality_score": 85
        }
    ],
    "Python Basics": [
        {
            "title": "Python Syntax Tutorial",
            "url": "https://www.w3schools.com/python/python_syntax.asp",
            "description": "Learn Python syntax and basic structure",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "Python Variables and Data Types",
            "url": "https://docs.python.org/3/tutorial/introduction.html",
            "description": "Official guide to Python variables and data types",
            "resource_type": "documentation",
            "quality_score": 92
        },
        {
            "title": "Python Beginner Exercises",
            "url": "https://www.w3resource.com/python-exercises/python-basic-exercises.php",
            "description": "Free practice exercises for Python beginners",
            "resource_type": "course",
            "quality_score": 85
        },
        {
            "title": "Python Input/Output Tutorial",
            "url": "https://realpython.com/python-input-output/",
            "description": "Learn Python input and output operations",
            "resource_type": "article",
            "quality_score": 87
        }
    ],
    "Control Structures": [
        {
            "title": "Python if/else Statements",
            "url": "https://docs.python.org/3/tutorial/controlflow.html",
            "description": "Official guide to Python control flow statements",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Python Loops Tutorial",
            "url": "https://www.w3schools.com/python/python_for_loops.asp",
            "description": "Learn for loops, while loops, and loop control",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "Conditional Logic in Python",
            "url": "https://realpython.com/python-conditional-statements/",
            "description": "Master Python conditional statements",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "Python Control Flow Exercises",
            "url": "https://pynative.com/python-if-else-and-for-loop-exercise/",
            "description": "Practice exercises for control structures",
            "resource_type": "course",
            "quality_score": 85
        }
    ],
    "Functions": [
        {
            "title": "Python Functions",
            "url": "https://docs.python.org/3/tutorial/controlflow.html#defining-functions",
            "description": "Official Python functions tutorial",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Python Function Arguments",
            "url": "https://realpython.com/python-kwargs-and-args/",
            "description": "Master *args, **kwargs, and function parameters",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "Lambda Functions in Python",
            "url": "https://www.w3schools.com/python/python_lambda.asp",
            "description": "Learn lambda functions and functional programming",
            "resource_type": "course",
            "quality_score": 87
        },
        {
            "title": "Python Function Exercises",
            "url": "https://pynative.com/python-functions-exercise/",
            "description": "Practice problems for Python functions",
            "resource_type": "course",
            "quality_score": 85
        }
    ],
    "Object-Oriented Programming": [
        {
            "title": "Python Classes and Objects",
            "url": "https://docs.python.org/3/tutorial/classes.html",
            "description": "Official Python OOP tutorial",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "OOP in Python - Real Python",
            "url": "https://realpython.com/python3-object-oriented-programming/",
            "description": "Comprehensive guide to Python OOP concepts",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Python Inheritance Tutorial",
            "url": "https://www.w3schools.com/python/python_inheritance.asp",
            "description": "Learn inheritance and polymorphism in Python",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "Python OOP Exercises",
            "url": "https://pynative.com/python-object-oriented-programming-oop-exercise/",
            "description": "Practice exercises for Python OOP",
            "resource_type": "course",
            "quality_score": 85
        }
    ],
    "JavaScript": [
        {
            "title": "MDN JavaScript Guide",
            "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide",
            "description": "Comprehensive free JavaScript guide by Mozilla",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "JavaScript.info",
            "url": "https://javascript.info/",
            "description": "Free modern JavaScript tutorial with interactive examples",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "freeCodeCamp JavaScript",
            "url": "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/",
            "description": "Free interactive JavaScript course with certification",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "Eloquent JavaScript",
            "url": "https://eloquentjavascript.net/",
            "description": "Free online book about JavaScript and programming",
            "resource_type": "article",
            "quality_score": 88
        }
    ],
    "JavaScript Fundamentals": [
        {
            "title": "JavaScript Basics - MDN",
            "url": "https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics",
            "description": "Learn JavaScript syntax and basic concepts",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "JavaScript Variables and Types",
            "url": "https://javascript.info/variables",
            "description": "Understanding variables, let, const, and data types",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "JavaScript First Steps",
            "url": "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-javascript/",
            "description": "Interactive JavaScript basics with exercises",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "JavaScript Tutorial - W3Schools",
            "url": "https://www.w3schools.com/js/js_intro.asp",
            "description": "Beginner-friendly JavaScript introduction",
            "resource_type": "course",
            "quality_score": 85
        }
    ],
    "DOM Manipulation": [
        {
            "title": "DOM Manipulation - MDN",
            "url": "https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Manipulating_documents",
            "description": "Official guide to DOM manipulation",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "JavaScript DOM Tutorial",
            "url": "https://javascript.info/document",
            "description": "Comprehensive DOM manipulation guide",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "DOM Manipulation Exercises",
            "url": "https://www.freecodecamp.org/news/how-to-manipulate-the-dom-beginners-guide/",
            "description": "Practical DOM manipulation examples",
            "resource_type": "article",
            "quality_score": 88
        },
        {
            "title": "Interactive DOM Practice",
            "url": "https://www.w3schools.com/js/js_htmldom.asp",
            "description": "Practice DOM manipulation with examples",
            "resource_type": "course",
            "quality_score": 85
        }
    ],
    "Asynchronous JavaScript": [
        {
            "title": "Promises and Async/Await - MDN",
            "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises",
            "description": "Master asynchronous JavaScript concepts",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Async JavaScript Tutorial",
            "url": "https://javascript.info/async",
            "description": "Complete guide to async programming in JavaScript",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Fetch API Tutorial",
            "url": "https://www.freecodecamp.org/news/how-to-use-fetch-api/",
            "description": "Learn to make HTTP requests with fetch",
            "resource_type": "article",
            "quality_score": 88
        },
        {
            "title": "Async JavaScript Exercises",
            "url": "https://www.codewars.com/collections/async-javascript",
            "description": "Practice problems for async JavaScript",
            "resource_type": "course",
            "quality_score": 85
        }
    ],
    "React": [
        {
            "title": "React Official Documentation",
            "url": "https://react.dev/learn",
            "description": "Official free React documentation and tutorial",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "React Tutorial - freeCodeCamp",
            "url": "https://www.freecodecamp.org/learn/front-end-development-libraries/react/",
            "description": "Free comprehensive React course with certification",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "React Tutorial for Beginners",
            "url": "https://www.w3schools.com/react/",
            "description": "Free step-by-step React tutorial",
            "resource_type": "course",
            "quality_score": 85
        },
        {
            "title": "React Handbook",
            "url": "https://reacthandbook.com/",
            "description": "Free comprehensive React guide",
            "resource_type": "article",
            "quality_score": 88
        }
    ],
    "HTML": [
        {
            "title": "MDN HTML Guide",
            "url": "https://developer.mozilla.org/en-US/docs/Web/HTML",
            "description": "Complete free HTML documentation by Mozilla",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "HTML Tutorial - W3Schools",
            "url": "https://www.w3schools.com/html/",
            "description": "Free interactive HTML tutorial with examples",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "HTML for Beginners - freeCodeCamp",
            "url": "https://www.freecodecamp.org/learn/responsive-web-design/basic-html-and-html5/",
            "description": "Free HTML course with hands-on practice",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "HTML5 Tutorial",
            "url": "https://htmldog.com/guides/html/",
            "description": "Free comprehensive HTML guide",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "CSS": [
        {
            "title": "MDN CSS Guide",
            "url": "https://developer.mozilla.org/en-US/docs/Web/CSS",
            "description": "Complete free CSS documentation by Mozilla",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "CSS Tutorial - W3Schools",
            "url": "https://www.w3schools.com/css/",
            "description": "Free interactive CSS tutorial with examples",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "CSS for Beginners - freeCodeCamp",
            "url": "https://www.freecodecamp.org/learn/responsive-web-design/basic-css/",
            "description": "Free CSS course with practical projects",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "CSS-Tricks Guide",
            "url": "https://css-tricks.com/guides/",
            "description": "Free comprehensive CSS guides and tutorials",
            "resource_type": "article",
            "quality_score": 87
        }
    ],
    "Machine Learning": [
        {
            "title": "Machine Learning Course - Andrew Ng",
            "url": "https://www.coursera.org/learn/machine-learning",
            "description": "Free audit of Andrew Ng's famous ML course (audit for free)",
            "resource_type": "course",
            "quality_score": 95
        },
        {
            "title": "Scikit-learn Tutorial",
            "url": "https://scikit-learn.org/stable/tutorial/index.html",
            "description": "Free official scikit-learn tutorials and documentation",
            "resource_type": "documentation",
            "quality_score": 90
        },
        {
            "title": "Machine Learning Mastery",
            "url": "https://machinelearningmastery.com/start-here/",
            "description": "Free comprehensive ML tutorials and guides",
            "resource_type": "article",
            "quality_score": 88
        },
        {
            "title": "Kaggle Learn - ML",
            "url": "https://www.kaggle.com/learn/intro-to-machine-learning",
            "description": "Free micro-courses in machine learning",
            "resource_type": "course",
            "quality_score": 87
        }
    ],
    "Data Science": [
        {
            "title": "Python for Data Science Handbook",
            "url": "https://jakevdp.github.io/PythonDataScienceHandbook/",
            "description": "Free online book for data science with Python",
            "resource_type": "article",
            "quality_score": 92
        },
        {
            "title": "Kaggle Learn - Data Science",
            "url": "https://www.kaggle.com/learn",
            "description": "Free micro-courses in data science and ML",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "Data Science Course - freeCodeCamp",
            "url": "https://www.freecodecamp.org/learn/data-analysis-with-python/",
            "description": "Free data analysis with Python certification course",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "R for Data Science",
            "url": "https://r4ds.had.co.nz/",
            "description": "Free online book for data science with R",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "Data Science Fundamentals": [
        {
            "title": "Introduction to Data Science - Coursera",
            "url": "https://www.coursera.org/learn/what-is-datascience",
            "description": "Free introduction to data science concepts (audit for free)",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "Statistics for Data Science",
            "url": "https://www.khanacademy.org/math/statistics-probability",
            "description": "Free statistics course essential for data science",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "Data Science Fundamentals - Kaggle",
            "url": "https://www.kaggle.com/learn/intro-to-machine-learning",
            "description": "Free introduction to ML and data science",
            "resource_type": "course",
            "quality_score": 87
        },
        {
            "title": "Data Science Process Guide",
            "url": "https://www.datascience-pm.com/crisp-dm-2/",
            "description": "Understanding the data science methodology",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "Intermediate Data Science": [
        {
            "title": "Feature Engineering Course",
            "url": "https://www.kaggle.com/learn/feature-engineering",
            "description": "Free course on creating better features for ML",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "Pandas Tutorial",
            "url": "https://pandas.pydata.org/docs/getting_started/intro_tutorials/",
            "description": "Official pandas tutorial for data manipulation",
            "resource_type": "documentation",
            "quality_score": 92
        },
        {
            "title": "Data Visualization with Python",
            "url": "https://www.kaggle.com/learn/data-visualization",
            "description": "Free course on creating effective visualizations",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "SQL for Data Science",
            "url": "https://www.kaggle.com/learn/intro-to-sql",
            "description": "Free SQL course tailored for data analysis",
            "resource_type": "course",
            "quality_score": 87
        }
    ],
    "Practical Data Science": [
        {
            "title": "Kaggle Competitions",
            "url": "https://www.kaggle.com/competitions",
            "description": "Real-world data science problems to practice",
            "resource_type": "course",
            "quality_score": 95
        },
        {
            "title": "Google Colab Tutorials",
            "url": "https://colab.research.google.com/notebooks/intro.ipynb",
            "description": "Free cloud environment for data science projects",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "Data Science Portfolio Guide",
            "url": "https://www.dataquest.io/blog/build-a-data-science-portfolio/",
            "description": "How to build impressive data science projects",
            "resource_type": "article",
            "quality_score": 88
        },
        {
            "title": "A/B Testing Guide",
            "url": "https://www.kaggle.com/learn/a-b-testing",
            "description": "Free course on experimental design and testing",
            "resource_type": "course",
            "quality_score": 85
        }
    ],
    "Advanced Data Science": [
        {
            "title": "Deep Learning Specialization",
            "url": "https://www.coursera.org/specializations/deep-learning",
            "description": "Andrew Ng's deep learning course (audit for free)",
            "resource_type": "course",
            "quality_score": 95
        },
        {
            "title": "Time Series Analysis",
            "url": "https://www.kaggle.com/learn/time-series",
            "description": "Free course on analyzing temporal data",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "Natural Language Processing",
            "url": "https://huggingface.co/course/chapter1/1",
            "description": "Free comprehensive NLP course",
            "resource_type": "course",
            "quality_score": 92
        },
        {
            "title": "MLOps Fundamentals",
            "url": "https://madewithml.com/",
            "description": "Free course on production ML systems",
            "resource_type": "course",
            "quality_score": 88
        }
    ],
    "Data Science Best Practices": [
        {
            "title": "Clean Code for Data Science",
            "url": "https://www.kdnuggets.com/2020/03/data-science-clean-code.html",
            "description": "Writing maintainable data science code",
            "resource_type": "article",
            "quality_score": 88
        },
        {
            "title": "Data Ethics Course",
            "url": "https://ethics.fast.ai/",
            "description": "Free course on ethical considerations in data science",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "Reproducible Research",
            "url": "https://www.coursera.org/learn/reproducible-research",
            "description": "Best practices for reproducible data science",
            "resource_type": "course",
            "quality_score": 87
        },
        {
            "title": "Model Deployment Guide",
            "url": "https://christophergs.com/machine%20learning/2019/03/17/how-to-deploy-machine-learning-models/",
            "description": "Guide to deploying ML models in production",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "Data Structures": [
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
            "description": "Free interactive data structure and algorithm visualizations",
            "resource_type": "article",
            "quality_score": 95
        },
        {
            "title": "GeeksforGeeks Data Structures",
            "url": "https://www.geeksforgeeks.org/data-structures/",
            "description": "Free comprehensive data structures tutorials",
            "resource_type": "article",
            "quality_score": 88
        },
        {
            "title": "Algorithms Course - Princeton",
            "url": "https://www.coursera.org/learn/algorithms-part1",
            "description": "Free audit of Princeton's algorithms course",
            "resource_type": "course",
            "quality_score": 92
        },
        {
            "title": "Data Structures - freeCodeCamp",
            "url": "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/",
            "description": "Free data structures and algorithms with JavaScript",
            "resource_type": "course",
            "quality_score": 85
        }
    ],
    "Node.js": [
        {
            "title": "Node.js Official Documentation",
            "url": "https://nodejs.org/en/docs/",
            "description": "Free official Node.js documentation and guides",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Node.js Tutorial - W3Schools",
            "url": "https://www.w3schools.com/nodejs/",
            "description": "Free comprehensive Node.js tutorial",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "Learn Node.js - freeCodeCamp",
            "url": "https://www.freecodecamp.org/news/free-8-hour-node-express-course/",
            "description": "Free 8-hour Node.js and Express course",
            "resource_type": "course",
            "quality_score": 87
        },
        {
            "title": "Node.js Tutorial - GeeksforGeeks",
            "url": "https://www.geeksforgeeks.org/nodejs-tutorial/",
            "description": "Free Node.js tutorial with examples",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "Git": [
        {
            "title": "Git Official Tutorial",
            "url": "https://git-scm.com/docs/gittutorial",
            "description": "Free official Git tutorial and documentation",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Learn Git Branching",
            "url": "https://learngitbranching.js.org/",
            "description": "Free interactive Git tutorial with visual learning",
            "resource_type": "course",
            "quality_score": 92
        },
        {
            "title": "Git Handbook - GitHub",
            "url": "https://guides.github.com/introduction/git-handbook/",
            "description": "Free comprehensive Git guide by GitHub",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "Git Tutorial - Atlassian",
            "url": "https://www.atlassian.com/git/tutorials",
            "description": "Free comprehensive Git tutorials",
            "resource_type": "course",
            "quality_score": 88
        }
    ],
    "SQL": [
        {
            "title": "SQL Tutorial - W3Schools",
            "url": "https://www.w3schools.com/sql/",
            "description": "Free interactive SQL tutorial with examples",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "SQLBolt",
            "url": "https://sqlbolt.com/",
            "description": "Free interactive SQL lessons and exercises",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "SQL Course - freeCodeCamp",
            "url": "https://www.freecodecamp.org/learn/relational-database/",
            "description": "Free relational database and SQL certification course",
            "resource_type": "course",
            "quality_score": 87
        },
        {
            "title": "PostgreSQL Tutorial",
            "url": "https://www.postgresqltutorial.com/",
            "description": "Free comprehensive PostgreSQL tutorial",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "Algorithms": [
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
            "description": "Free interactive algorithm visualizations",
            "resource_type": "article",
            "quality_score": 90
        },
        {
            "title": "Algorithms - GeeksforGeeks",
            "url": "https://www.geeksforgeeks.org/fundamentals-of-algorithms/",
            "description": "Free comprehensive algorithms tutorials",
            "resource_type": "article",
            "quality_score": 88
        },
        {
            "title": "LeetCode Practice",
            "url": "https://leetcode.com/problemset/all/",
            "description": "Free algorithm practice problems (basic tier)",
            "resource_type": "course",
            "quality_score": 85
        }
    ],
    "Variables": [
        {
            "title": "Variables in Programming",
            "url": "https://developer.mozilla.org/en-US/docs/Glossary/Variable",
            "description": "Understanding variables in programming",
            "resource_type": "documentation",
            "quality_score": 85
        },
        {
            "title": "Python Variables Tutorial",
            "url": "https://www.w3schools.com/python/python_variables.asp",
            "description": "Learn about Python variables",
            "resource_type": "article",
            "quality_score": 80
        }
    ],
    "Data Types": [
        {
            "title": "Python Data Types",
            "url": "https://docs.python.org/3/library/stdtypes.html",
            "description": "Official Python data types documentation",
            "resource_type": "documentation",
            "quality_score": 90
        },
        {
            "title": "Understanding Data Types",
            "url": "https://www.w3schools.com/python/python_datatypes.asp",
            "description": "Learn about different data types",
            "resource_type": "article",
            "quality_score": 82
        }
    ],
    "Control Flow": [
        {
            "title": "Control Flow Statements",
            "url": "https://docs.python.org/3/tutorial/controlflow.html",
            "description": "Python control flow tutorial",
            "resource_type": "documentation",
            "quality_score": 90
        },
        {
            "title": "If, Elif, Else Statements",
            "url": "https://www.w3schools.com/python/python_conditions.asp",
            "description": "Learn conditional statements",
            "resource_type": "article",
            "quality_score": 80
        }
    ],
    "Functions": [
        {
            "title": "Python Functions",
            "url": "https://docs.python.org/3/tutorial/controlflow.html#defining-functions",
            "description": "Official Python functions tutorial",
            "resource_type": "documentation",
            "quality_score": 92
        },
        {
            "title": "Functions in Programming",
            "url": "https://www.w3schools.com/python/python_functions.asp",
            "description": "Learn how to create and use functions",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "OOP": [
        {
            "title": "Object-Oriented Programming in Python",
            "url": "https://docs.python.org/3/tutorial/classes.html",
            "description": "Official Python OOP tutorial",
            "resource_type": "documentation",
            "quality_score": 90
        },
        {
            "title": "Python OOP Concepts",
            "url": "https://www.w3schools.com/python/python_classes.asp",
            "description": "Learn object-oriented programming",
            "resource_type": "article",
            "quality_score": 83
        }
    ],
    "Java": [
        {
            "title": "Oracle Java Tutorial",
            "url": "https://docs.oracle.com/javase/tutorial/",
            "description": "Official Java tutorial from Oracle",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Java Programming - freeCodeCamp",
            "url": "https://www.freecodecamp.org/news/java-tutorial-for-beginners/",
            "description": "Complete Java programming course",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "Codecademy Java Course",
            "url": "https://www.codecademy.com/learn/learn-java",
            "description": "Interactive Java programming course",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "Java Code Examples",
            "url": "https://www.programiz.com/java-programming",
            "description": "Java programming examples and tutorials",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "C++": [
        {
            "title": "C++ Tutorial - cplusplus.com",
            "url": "https://www.cplusplus.com/doc/tutorial/",
            "description": "Comprehensive C++ programming tutorial",
            "resource_type": "documentation",
            "quality_score": 92
        },
        {
            "title": "Learn C++ - freeCodeCamp",
            "url": "https://www.freecodecamp.org/news/c-plus-plus-tutorial/",
            "description": "Complete C++ programming course",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "C++ Programming Examples",
            "url": "https://www.programiz.com/cpp-programming",
            "description": "C++ examples and practice problems",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "C#": [
        {
            "title": "Microsoft C# Documentation",
            "url": "https://docs.microsoft.com/en-us/dotnet/csharp/",
            "description": "Official C# documentation and tutorials",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "C# Tutorial - W3Schools",
            "url": "https://www.w3schools.com/cs/",
            "description": "Interactive C# tutorial with examples",
            "resource_type": "course",
            "quality_score": 88
        }
    ],
    "Go": [
        {
            "title": "Go by Example",
            "url": "https://gobyexample.com/",
            "description": "Hands-on introduction to Go programming",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "Tour of Go",
            "url": "https://tour.golang.org/",
            "description": "Interactive introduction to Go",
            "resource_type": "course",
            "quality_score": 92
        }
    ],
    "Rust": [
        {
            "title": "The Rust Programming Language Book",
            "url": "https://doc.rust-lang.org/book/",
            "description": "The official Rust programming language book",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Rust by Example",
            "url": "https://doc.rust-lang.org/stable/rust-by-example/",
            "description": "Learn Rust with examples",
            "resource_type": "course",
            "quality_score": 90
        }
    ],
    "Swift": [
        {
            "title": "Swift Programming Language Guide",
            "url": "https://docs.swift.org/swift-book/",
            "description": "Official Swift programming guide",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "100 Days of SwiftUI",
            "url": "https://www.hackingwithswift.com/100/swiftui",
            "description": "Free SwiftUI course",
            "resource_type": "course",
            "quality_score": 90
        }
    ],
    "Kotlin": [
        {
            "title": "Kotlin Documentation",
            "url": "https://kotlinlang.org/docs/",
            "description": "Official Kotlin documentation and tutorials",
            "resource_type": "documentation",
            "quality_score": 92
        },
        {
            "title": "Kotlin Koans",
            "url": "https://play.kotlinlang.org/koans/",
            "description": "Interactive Kotlin exercises",
            "resource_type": "course",
            "quality_score": 88
        }
    ],
    
    # Frameworks and Libraries
    "Angular": [
        {
            "title": "Angular Documentation",
            "url": "https://angular.io/docs",
            "description": "Official Angular documentation and tutorials",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Angular Tutorial - freeCodeCamp",
            "url": "https://www.freecodecamp.org/learn/front-end-development-libraries/",
            "description": "Complete Angular course",
            "resource_type": "course",
            "quality_score": 90
        }
    ],
    "Vue.js": [
        {
            "title": "Vue.js Guide",
            "url": "https://vuejs.org/guide/",
            "description": "Official Vue.js guide and documentation",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Vue Mastery",
            "url": "https://www.vuemastery.com/courses-path/beginner",
            "description": "Free Vue.js courses for beginners",
            "resource_type": "course",
            "quality_score": 90
        }
    ],
    "Django": [
        {
            "title": "Django Documentation",
            "url": "https://docs.djangoproject.com/en/stable/",
            "description": "Official Django documentation and tutorial",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Django for Beginners",
            "url": "https://djangoforbeginners.com/",
            "description": "Complete Django tutorial book",
            "resource_type": "article",
            "quality_score": 90
        }
    ],
    "Flask": [
        {
            "title": "Flask Documentation",
            "url": "https://flask.palletsprojects.com/",
            "description": "Official Flask documentation and quickstart",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Flask Mega-Tutorial",
            "url": "https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world",
            "description": "Comprehensive Flask tutorial series",
            "resource_type": "article",
            "quality_score": 92
        }
    ],
    
    # Data & Analytics
    "Excel": [
        {
            "title": "Excel Tutorial - ExcelJet",
            "url": "https://exceljet.net/excel-tutorial",
            "description": "Comprehensive Excel tutorials and tips",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "Microsoft Excel Help Center",
            "url": "https://support.microsoft.com/en-us/excel",
            "description": "Official Excel help and tutorials",
            "resource_type": "documentation",
            "quality_score": 88
        }
    ],
    "Tableau": [
        {
            "title": "Tableau Learning",
            "url": "https://www.tableau.com/learn",
            "description": "Free Tableau training and tutorials",
            "resource_type": "course",
            "quality_score": 92
        },
        {
            "title": "Tableau Public Training",
            "url": "https://public.tableau.com/en-us/s/resources",
            "description": "Free resources for Tableau Public",
            "resource_type": "course",
            "quality_score": 88
        }
    ],
    "Power BI": [
        {
            "title": "Microsoft Power BI Learning",
            "url": "https://docs.microsoft.com/en-us/power-bi/guided-learning/",
            "description": "Official Power BI guided learning",
            "resource_type": "course",
            "quality_score": 92
        },
        {
            "title": "Power BI YouTube Channel",
            "url": "https://www.youtube.com/user/mspowerbi",
            "description": "Official Power BI video tutorials",
            "resource_type": "video",
            "quality_score": 88
        }
    ],
    
    # Design & Creative
    "Photoshop": [
        {
            "title": "Adobe Photoshop Tutorials",
            "url": "https://helpx.adobe.com/photoshop/tutorials.html",
            "description": "Official Adobe Photoshop tutorials",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "GIMP Alternative Tutorial",
            "url": "https://www.gimp.org/tutorials/",
            "description": "Free alternative to Photoshop with tutorials",
            "resource_type": "course",
            "quality_score": 85
        }
    ],
    "Figma": [
        {
            "title": "Figma Academy",
            "url": "https://www.figma.com/academy/",
            "description": "Official Figma design tutorials",
            "resource_type": "course",
            "quality_score": 92
        },
        {
            "title": "Figma Tutorial - freeCodeCamp",
            "url": "https://www.youtube.com/watch?v=jwCmIBJ8Jtc",
            "description": "Complete Figma course for beginners",
            "resource_type": "video",
            "quality_score": 88
        }
    ],
    "UI/UX Design": [
        {
            "title": "Google UX Design Certificate",
            "url": "https://www.coursera.org/professional-certificates/google-ux-design",
            "description": "Professional UX design course (audit for free)",
            "resource_type": "course",
            "quality_score": 95
        },
        {
            "title": "UX Design Fundamentals",
            "url": "https://www.interaction-design.org/",
            "description": "Free UX design courses and articles",
            "resource_type": "course",
            "quality_score": 90
        }
    ],
    
    # Cloud & DevOps
    "AWS": [
        {
            "title": "AWS Training and Certification",
            "url": "https://aws.amazon.com/training/",
            "description": "Free AWS training courses and labs",
            "resource_type": "course",
            "quality_score": 95
        },
        {
            "title": "AWS Cloud Practitioner Essentials",
            "url": "https://aws.amazon.com/training/course-descriptions/cloud-practitioner-essentials/",
            "description": "Free foundational AWS course",
            "resource_type": "course",
            "quality_score": 92
        }
    ],
    "Docker": [
        {
            "title": "Docker Documentation",
            "url": "https://docs.docker.com/",
            "description": "Official Docker documentation and tutorials",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Docker Tutorial for Beginners",
            "url": "https://www.youtube.com/watch?v=fqMOX6JJhGo",
            "description": "Complete Docker course",
            "resource_type": "video",
            "quality_score": 90
        }
    ],
    "Kubernetes": [
        {
            "title": "Kubernetes Documentation",
            "url": "https://kubernetes.io/docs/home/",
            "description": "Official Kubernetes documentation",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Kubernetes Tutorial - freeCodeCamp",
            "url": "https://www.freecodecamp.org/news/learn-kubernetes-in-under-3-hours-a-detailed-guide-to-orchestrating-containers/",
            "description": "Complete Kubernetes tutorial",
            "resource_type": "course",
            "quality_score": 90
        }
    ],
    
    # Mobile Development
    "Android Development": [
        {
            "title": "Android Developer Guides",
            "url": "https://developer.android.com/guide",
            "description": "Official Android development documentation",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Android Development - Udacity",
            "url": "https://www.udacity.com/course/android-kotlin-developer-nanodegree--nd940",
            "description": "Free Android development courses",
            "resource_type": "course",
            "quality_score": 90
        }
    ],
    "iOS Development": [
        {
            "title": "Apple Developer Documentation",
            "url": "https://developer.apple.com/documentation/",
            "description": "Official iOS development documentation",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "iOS Development Tutorial",
            "url": "https://www.raywenderlich.com/ios",
            "description": "Comprehensive iOS development tutorials",
            "resource_type": "course",
            "quality_score": 90
        }
    ],
    "React Native": [
        {
            "title": "React Native Documentation",
            "url": "https://reactnative.dev/docs/getting-started",
            "description": "Official React Native documentation",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "React Native Tutorial",
            "url": "https://www.freecodecamp.org/news/create-an-app-with-react-native/",
            "description": "Complete React Native course",
            "resource_type": "course",
            "quality_score": 90
        }
    ],
    "Flutter": [
        {
            "title": "Flutter Documentation",
            "url": "https://flutter.dev/docs",
            "description": "Official Flutter documentation and tutorials",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Flutter Course - freeCodeCamp",
            "url": "https://www.freecodecamp.org/news/learn-flutter-full-course/",
            "description": "Complete Flutter development course",
            "resource_type": "course",
            "quality_score": 90
        }
    ],
    
    # Business & Soft Skills
    "Digital Marketing": [
        {
            "title": "Google Digital Marketing Course",
            "url": "https://learndigital.withgoogle.com/digitalgarage",
            "description": "Free digital marketing certification from Google",
            "resource_type": "course",
            "quality_score": 95
        },
        {
            "title": "HubSpot Academy",
            "url": "https://academy.hubspot.com/",
            "description": "Free marketing, sales, and service courses",
            "resource_type": "course",
            "quality_score": 90
        }
    ],
    "Project Management": [
        {
            "title": "Google Project Management Certificate",
            "url": "https://www.coursera.org/professional-certificates/google-project-management",
            "description": "Professional project management course (audit for free)",
            "resource_type": "course",
            "quality_score": 95
        },
        {
            "title": "PMI Resources",
            "url": "https://www.pmi.org/learning/library",
            "description": "Project management resources and guides",
            "resource_type": "article",
            "quality_score": 88
        }
    ],
    "Public Speaking": [
        {
            "title": "Toastmasters International",
            "url": "https://www.toastmasters.org/pathways-overview",
            "description": "Public speaking and leadership development",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "TED Masterclass",
            "url": "https://www.ted.com/playlists/574/how_to_make_a_great_presentation",
            "description": "Learn from the best TED speakers",
            "resource_type": "video",
            "quality_score": 88
        }
    ],

    # Additional Programming Languages
    "Java": [
        {
            "title": "Oracle Java Tutorial",
            "url": "https://docs.oracle.com/javase/tutorial/",
            "description": "Official Java tutorial from Oracle",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Java Programming - freeCodeCamp",
            "url": "https://www.freecodecamp.org/news/java-tutorial-for-beginners/",
            "description": "Complete Java programming course",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "Codecademy Java Course",
            "url": "https://www.codecademy.com/learn/learn-java",
            "description": "Interactive Java programming course",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "Java Code Examples",
            "url": "https://www.programiz.com/java-programming",
            "description": "Java programming examples and tutorials",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "C++": [
        {
            "title": "C++ Tutorial - cplusplus.com",
            "url": "https://www.cplusplus.com/doc/tutorial/",
            "description": "Comprehensive C++ programming tutorial",
            "resource_type": "documentation",
            "quality_score": 92
        },
        {
            "title": "Learn C++ - freeCodeCamp",
            "url": "https://www.freecodecamp.org/news/c-plus-plus-tutorial/",
            "description": "Complete C++ programming course",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "C++ Programming Examples",
            "url": "https://www.programiz.com/cpp-programming",
            "description": "C++ examples and practice problems",
            "resource_type": "article",
            "quality_score": 85
        }
    ],
    "C#": [
        {
            "title": "Microsoft C# Documentation",
            "url": "https://docs.microsoft.com/en-us/dotnet/csharp/",
            "description": "Official C# documentation and tutorials",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "C# Tutorial - W3Schools",
            "url": "https://www.w3schools.com/cs/",
            "description": "Interactive C# tutorial with examples",
            "resource_type": "course",
            "quality_score": 88
        }
    ],
    "Go": [
        {
            "title": "Go by Example",
            "url": "https://gobyexample.com/",
            "description": "Hands-on introduction to Go programming",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "Tour of Go",
            "url": "https://tour.golang.org/",
            "description": "Interactive introduction to Go",
            "resource_type": "course",
            "quality_score": 92
        }
    ],
    "Rust": [
        {
            "title": "The Rust Programming Language Book",
            "url": "https://doc.rust-lang.org/book/",
            "description": "The official Rust programming language book",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Rust by Example",
            "url": "https://doc.rust-lang.org/stable/rust-by-example/",
            "description": "Learn Rust with examples",
            "resource_type": "course",
            "quality_score": 90
        }
    ],
    "Swift": [
        {
            "title": "Swift Programming Language Guide",
            "url": "https://docs.swift.org/swift-book/",
            "description": "Official Swift programming guide",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "100 Days of SwiftUI",
            "url": "https://www.hackingwithswift.com/100/swiftui",
            "description": "Free SwiftUI course",
            "resource_type": "course",
            "quality_score": 90
        }
    ],
    "Kotlin": [
        {
            "title": "Kotlin Documentation",
            "url": "https://kotlinlang.org/docs/",
            "description": "Official Kotlin documentation and tutorials",
            "resource_type": "documentation",
            "quality_score": 92
        },
        {
            "title": "Kotlin Koans",
            "url": "https://play.kotlinlang.org/koans/",
            "description": "Interactive Kotlin exercises",
            "resource_type": "course",
            "quality_score": 88
        }
    ],
    
    # Frameworks and Libraries
    "Angular": [
        {
            "title": "Angular Documentation",
            "url": "https://angular.io/docs",
            "description": "Official Angular documentation and tutorials",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Angular Tutorial - freeCodeCamp",
            "url": "https://www.freecodecamp.org/learn/front-end-development-libraries/",
            "description": "Complete Angular course",
            "resource_type": "course",
            "quality_score": 90
        }
    ],
    "Vue.js": [
        {
            "title": "Vue.js Guide",
            "url": "https://vuejs.org/guide/",
            "description": "Official Vue.js guide and documentation",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Vue Mastery",
            "url": "https://www.vuemastery.com/courses-path/beginner",
            "description": "Free Vue.js courses for beginners",
            "resource_type": "course",
            "quality_score": 90
        }
    ],
    "Django": [
        {
            "title": "Django Documentation",
            "url": "https://docs.djangoproject.com/en/stable/",
            "description": "Official Django documentation and tutorial",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Django for Beginners",
            "url": "https://djangoforbeginners.com/",
            "description": "Complete Django tutorial book",
            "resource_type": "article",
            "quality_score": 90
        }
    ],
    "Flask": [
        {
            "title": "Flask Documentation",
            "url": "https://flask.palletsprojects.com/",
            "description": "Official Flask documentation and quickstart",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Flask Mega-Tutorial",
            "url": "https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world",
            "description": "Comprehensive Flask tutorial series",
            "resource_type": "article",
            "quality_score": 92
        }
    ],
    
    # Data & Analytics
    "Excel": [
        {
            "title": "Excel Tutorial - ExcelJet",
            "url": "https://exceljet.net/excel-tutorial",
            "description": "Comprehensive Excel tutorials and tips",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "Microsoft Excel Help Center",
            "url": "https://support.microsoft.com/en-us/excel",
            "description": "Official Excel help and tutorials",
            "resource_type": "documentation",
            "quality_score": 88
        }
    ],
    "Tableau": [
        {
            "title": "Tableau Learning",
            "url": "https://www.tableau.com/learn",
            "description": "Free Tableau training and tutorials",
            "resource_type": "course",
            "quality_score": 92
        },
        {
            "title": "Tableau Public Training",
            "url": "https://public.tableau.com/en-us/s/resources",
            "description": "Free resources for Tableau Public",
            "resource_type": "course",
            "quality_score": 88
        }
    ],
    "Power BI": [
        {
            "title": "Microsoft Power BI Learning",
            "url": "https://docs.microsoft.com/en-us/power-bi/guided-learning/",
            "description": "Official Power BI guided learning",
            "resource_type": "course",
            "quality_score": 92
        },
        {
            "title": "Power BI YouTube Channel",
            "url": "https://www.youtube.com/user/mspowerbi",
            "description": "Official Power BI video tutorials",
            "resource_type": "video",
            "quality_score": 88
        }
    ],
    
    # Design & Creative
    "Photoshop": [
        {
            "title": "Adobe Photoshop Tutorials",
            "url": "https://helpx.adobe.com/photoshop/tutorials.html",
            "description": "Official Adobe Photoshop tutorials",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "GIMP Alternative Tutorial",
            "url": "https://www.gimp.org/tutorials/",
            "description": "Free alternative to Photoshop with tutorials",
            "resource_type": "course",
            "quality_score": 85
        }
    ],
    "Figma": [
        {
            "title": "Figma Academy",
            "url": "https://www.figma.com/academy/",
            "description": "Official Figma design tutorials",
            "resource_type": "course",
            "quality_score": 92
        },
        {
            "title": "Figma Tutorial - freeCodeCamp",
            "url": "https://www.youtube.com/watch?v=jwCmIBJ8Jtc",
            "description": "Complete Figma course for beginners",
            "resource_type": "video",
            "quality_score": 88
        }
    ],
    "UI/UX Design": [
        {
            "title": "Google UX Design Certificate",
            "url": "https://www.coursera.org/professional-certificates/google-ux-design",
            "description": "Professional UX design course (audit for free)",
            "resource_type": "course",
            "quality_score": 95
        },
        {
            "title": "UX Design Fundamentals",
            "url": "https://www.interaction-design.org/",
            "description": "Free UX design courses and articles",
            "resource_type": "course",
            "quality_score": 90
        }
    ],
    
    # Cloud & DevOps
    "AWS": [
        {
            "title": "AWS Training and Certification",
            "url": "https://aws.amazon.com/training/",
            "description": "Free AWS training courses and labs",
            "resource_type": "course",
            "quality_score": 95
        },
        {
            "title": "AWS Cloud Practitioner Essentials",
            "url": "https://aws.amazon.com/training/course-descriptions/cloud-practitioner-essentials/",
            "description": "Free foundational AWS course",
            "resource_type": "course",
            "quality_score": 92
        }
    ],
    "Docker": [
        {
            "title": "Docker Documentation",
            "url": "https://docs.docker.com/",
            "description": "Official Docker documentation and tutorials",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Docker Tutorial for Beginners",
            "url": "https://www.youtube.com/watch?v=fqMOX6JJhGo",
            "description": "Complete Docker course",
            "resource_type": "video",
            "quality_score": 90
        }
    ],
    "Kubernetes": [
        {
            "title": "Kubernetes Documentation",
            "url": "https://kubernetes.io/docs/home/",
            "description": "Official Kubernetes documentation",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Kubernetes Tutorial - freeCodeCamp",
            "url": "https://www.freecodecamp.org/news/learn-kubernetes-in-under-3-hours-a-detailed-guide-to-orchestrating-containers/",
            "description": "Complete Kubernetes tutorial",
            "resource_type": "course",
            "quality_score": 90
        }
    ],
    
    # Mobile Development
    "Android Development": [
        {
            "title": "Android Developer Guides",
            "url": "https://developer.android.com/guide",
            "description": "Official Android development documentation",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Android Development - Udacity",
            "url": "https://www.udacity.com/course/android-kotlin-developer-nanodegree--nd940",
            "description": "Free Android development courses",
            "resource_type": "course",
            "quality_score": 90
        }
    ],
    "iOS Development": [
        {
            "title": "Apple Developer Documentation",
            "url": "https://developer.apple.com/documentation/",
            "description": "Official iOS development documentation",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "iOS Development Tutorial",
            "url": "https://www.raywenderlich.com/ios",
            "description": "Comprehensive iOS development tutorials",
            "resource_type": "course",
            "quality_score": 90
        }
    ],
    "React Native": [
        {
            "title": "React Native Documentation",
            "url": "https://reactnative.dev/docs/getting-started",
            "description": "Official React Native documentation",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "React Native Tutorial",
            "url": "https://www.freecodecamp.org/news/create-an-app-with-react-native/",
            "description": "Complete React Native course",
            "resource_type": "course",
            "quality_score": 90
        }
    ],
    "Flutter": [
        {
            "title": "Flutter Documentation",
            "url": "https://flutter.dev/docs",
            "description": "Official Flutter documentation and tutorials",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Flutter Course - freeCodeCamp",
            "url": "https://www.freecodecamp.org/news/learn-flutter-full-course/",
            "description": "Complete Flutter development course",
            "resource_type": "course",
            "quality_score": 90
        }
    ],
    
    # Business & Soft Skills
    "Digital Marketing": [
        {
            "title": "Google Digital Marketing Course",
            "url": "https://learndigital.withgoogle.com/digitalgarage",
            "description": "Free digital marketing certification from Google",
            "resource_type": "course",
            "quality_score": 95
        },
        {
            "title": "HubSpot Academy",
            "url": "https://academy.hubspot.com/",
            "description": "Free marketing, sales, and service courses",
            "resource_type": "course",
            "quality_score": 90
        }
    ],
    "Project Management": [
        {
            "title": "Google Project Management Certificate",
            "url": "https://www.coursera.org/professional-certificates/google-project-management",
            "description": "Professional project management course (audit for free)",
            "resource_type": "course",
            "quality_score": 95
        },
        {
            "title": "PMI Resources",
            "url": "https://www.pmi.org/learning/library",
            "description": "Project management resources and guides",
            "resource_type": "article",
            "quality_score": 88
        }
    ],
    "Public Speaking": [
        {
            "title": "Toastmasters International",
            "url": "https://www.toastmasters.org/pathways-overview",
            "description": "Public speaking and leadership development",
            "resource_type": "course",
            "quality_score": 90
        },
        {
            "title": "TED Masterclass",
            "url": "https://www.ted.com/playlists/574/how_to_make_a_great_presentation",
            "description": "Learn from the best TED speakers",
            "resource_type": "video",
            "quality_score": 88
        }
    ]
}

# Platform availability mapping - only include platforms that actually have content for these skill types
PLATFORM_SKILL_MAPPING = {
    'youtube': ['*'],  # YouTube has content for everything
    'khan_academy': ['math', 'science', 'programming', 'economics', 'history', 'art', 'computing', 'test prep'],
    'coursera': ['programming', 'data science', 'business', 'language', 'health', 'arts', 'social science', 'physical science'],
    'edx': ['computer science', 'engineering', 'data science', 'business', 'language', 'science', 'math'],
    'freecodecamp': ['programming', 'web development', 'data science', 'coding', 'javascript', 'python', 'html', 'css'],
    'github': ['programming', 'development', 'coding', 'software', 'web development', 'data science'],
    'mdn': ['web development', 'javascript', 'html', 'css', 'programming', 'frontend'],
    'w3schools': ['web development', 'programming', 'html', 'css', 'javascript', 'sql'],
    'codecademy': ['programming', 'web development', 'data science', 'coding'],
    'udacity': ['programming', 'data science', 'ai', 'business', 'digital marketing'],
    'pluralsight': ['technology', 'programming', 'creative', 'business'],
    'skillshare': ['creative', 'design', 'business', 'lifestyle', 'photography'],
    'masterclass': ['creative', 'cooking', 'music', 'writing', 'business', 'lifestyle'],
    'domestika': ['creative', 'design', 'illustration', 'photography', 'crafts'],
    'adobe_tutorials': ['design', 'creative', 'photography', 'video', 'art'],
    'behance': ['design', 'creative', 'art', 'photography'],
    'dribbble': ['design', 'ui', 'ux', 'creative'],
    'figma_academy': ['design', 'ui', 'ux', 'prototyping'],
    'hubspot': ['marketing', 'business', 'sales', 'customer service'],
    'google_skillshop': ['marketing', 'advertising', 'analytics', 'business'],
    'linkedin_learning': ['business', 'technology', 'creative'],
    'allrecipes': ['cooking', 'baking', 'food', 'culinary'],
    'food_network': ['cooking', 'baking', 'culinary'],
    'fitness_blender': ['fitness', 'exercise', 'health', 'workout'],
    'yoga_with_adriene': ['yoga', 'fitness', 'meditation', 'wellness'],
    'ultimate_guitar': ['music', 'guitar', 'instrument'],
    'musictheory': ['music', 'theory', 'instrument'],
    'wikihow': ['*'],  # WikiHow has guides for most things
    'reddit': ['*']    # Reddit has communities for most topics
}

def check_platform_relevance(skill_lower, platform_skills):
    """Check if a platform is relevant for the given skill"""
    if '*' in platform_skills:
        return True
    
    for platform_skill in platform_skills:
        if platform_skill in skill_lower:
            return True
    return False

def generate_universal_resources(skill_name):
    """Generate high-quality free resources for ANY skill, but only from platforms that actually have that content"""
    skill_clean = skill_name.strip()
    skill_url_safe = skill_clean.lower().replace(' ', '-').replace('/', '-')
    skill_lower = skill_clean.lower()
    
    resources = []
    
    # Always include YouTube (has content for everything)
    resources.append({
        "title": f"YouTube - {skill_clean} Tutorial",
        "url": f"https://www.youtube.com/results?search_query={skill_url_safe}+tutorial",
        "description": f"Free video tutorials and courses for {skill_clean}",
        "resource_type": "video",
        "quality_score": 85
    })
    
    # Check Khan Academy relevance
    if check_platform_relevance(skill_lower, PLATFORM_SKILL_MAPPING['khan_academy']):
        resources.append({
            "title": f"Khan Academy - {skill_clean}",
            "url": f"https://www.khanacademy.org/search?search_again=1&page_search_query={skill_url_safe}",
            "description": f"Free interactive lessons and practice for {skill_clean}",
            "resource_type": "course",
            "quality_score": 88
        })
    
    # Check Coursera relevance  
    if check_platform_relevance(skill_lower, PLATFORM_SKILL_MAPPING['coursera']):
        resources.append({
            "title": f"Coursera - {skill_clean} (Free Audit)",
            "url": f"https://www.coursera.org/search?query={skill_url_safe}",
            "description": f"University-level courses for {skill_clean} (audit for free)",
            "resource_type": "course",
            "quality_score": 92
        })
    
    # Check edX relevance
    if check_platform_relevance(skill_lower, PLATFORM_SKILL_MAPPING['edx']):
        resources.append({
            "title": f"edX - {skill_clean} Courses",
            "url": f"https://www.edx.org/search?q={skill_url_safe}",
            "description": f"Free online courses from top universities for {skill_clean}",
            "resource_type": "course",
            "quality_score": 90
        })
    
    # Add skill-specific platforms based on skill type
    if any(term in skill_lower for term in ['programming', 'coding', 'development', 'python', 'javascript', 'java', 'c++', 'software', 'web development', 'html', 'css']):
        if check_platform_relevance(skill_lower, PLATFORM_SKILL_MAPPING['freecodecamp']):
            resources.append({
                "title": f"freeCodeCamp - {skill_clean}",
                "url": f"https://www.freecodecamp.org/learn",
                "description": f"Free comprehensive programming course for {skill_clean}",
                "resource_type": "course",
                "quality_score": 90
            })
        
        if check_platform_relevance(skill_lower, PLATFORM_SKILL_MAPPING['github']):
            resources.append({
                "title": f"GitHub - {skill_clean} Projects",
                "url": f"https://github.com/search?q={skill_url_safe}+tutorial",
                "description": f"Open source projects and examples for {skill_clean}",
                "resource_type": "project",
                "quality_score": 87
            })
        
        if check_platform_relevance(skill_lower, PLATFORM_SKILL_MAPPING['mdn']):
            resources.append({
                "title": f"MDN Web Docs - {skill_clean}",
                "url": f"https://developer.mozilla.org/en-US/search?q={skill_url_safe}",
                "description": f"Comprehensive documentation for {skill_clean}",
                "resource_type": "documentation",
                "quality_score": 94
            })
            
    elif any(term in skill_lower for term in ['music', 'guitar', 'piano', 'singing', 'instrument']):
        if 'guitar' in skill_lower:
            resources.append({
                "title": f"Ultimate Guitar - {skill_clean}",
                "url": f"https://www.ultimate-guitar.com/",
                "description": f"Free guitar tutorials and tabs for {skill_clean}",
                "resource_type": "course",
                "quality_score": 85
            })
        
        resources.append({
            "title": f"Musictheory.net - {skill_clean}",
            "url": f"https://www.musictheory.net/",
            "description": f"Free music theory and practice for {skill_clean}",
            "resource_type": "course",
            "quality_score": 88
        })
        
    elif any(term in skill_lower for term in ['photography', 'photo']):
        resources.append({
            "title": f"PetaPixel - {skill_clean}",
            "url": f"https://petapixel.com/",
            "description": f"Photography tutorials and tips for {skill_clean}",
            "resource_type": "article",
            "quality_score": 88
        })
        
        resources.append({
            "title": f"Digital Photography School",
            "url": f"https://digital-photography-school.com/",
            "description": f"Free photography tutorials and guides for {skill_clean}",
            "resource_type": "course",
            "quality_score": 85
        })
            
    elif any(term in skill_lower for term in ['design', 'photoshop', 'illustrator', 'figma', 'ui', 'ux', 'creative', 'art', 'graphic']):
        resources.append({
            "title": f"Behance - {skill_clean} Inspiration",
            "url": f"https://www.behance.net/search/projects?search={skill_url_safe}",
            "description": f"Creative inspiration and tutorials for {skill_clean}",
            "resource_type": "article",
            "quality_score": 85
        })
        
        if 'design' in skill_lower or 'ui' in skill_lower or 'ux' in skill_lower:
            resources.append({
                "title": f"Figma Academy - {skill_clean}",
                "url": f"https://www.figma.com/academy/",
                "description": f"Professional design tutorials for {skill_clean}",
                "resource_type": "course",
                "quality_score": 88
            })
        
    elif any(term in skill_lower for term in ['business', 'marketing', 'management', 'finance', 'economics', 'sales']):
        if 'marketing' in skill_lower or 'advertising' in skill_lower:
            resources.append({
                "title": f"HubSpot Academy - {skill_clean}",
                "url": f"https://academy.hubspot.com/",
                "description": f"Free business and marketing courses for {skill_clean}",
                "resource_type": "course",
                "quality_score": 90
            })
        
        resources.append({
            "title": f"Google Digital Garage - {skill_clean}",
            "url": f"https://learndigital.withgoogle.com/digitalgarage",
            "description": f"Free professional development courses for {skill_clean}",
            "resource_type": "course",
            "quality_score": 88
        })
        
    elif any(term in skill_lower for term in ['cooking', 'baking', 'recipe', 'culinary', 'chef']):
        resources.append({
            "title": f"Allrecipes - {skill_clean}",
            "url": f"https://www.allrecipes.com/search/results/?search={skill_url_safe}",
            "description": f"Free recipes and cooking tutorials for {skill_clean}",
            "resource_type": "article",
            "quality_score": 85
        })
        
        resources.append({
            "title": f"Food Network - {skill_clean}",
            "url": f"https://www.foodnetwork.com/search/{skill_url_safe}-",
            "description": f"Professional cooking tutorials for {skill_clean}",
            "resource_type": "video",
            "quality_score": 88
        })
        
    elif any(term in skill_lower for term in ['fitness', 'exercise', 'workout', 'yoga', 'health', 'training']):
        if 'yoga' in skill_lower or 'meditation' in skill_lower:
            resources.append({
                "title": f"Yoga with Adriene - {skill_clean}",
                "url": f"https://yogawithadriene.com/",
                "description": f"Free yoga and wellness content for {skill_clean}",
                "resource_type": "video",
                "quality_score": 90
            })
        else:
            resources.append({
                "title": f"Fitness Blender - {skill_clean}",
                "url": f"https://www.fitnessblender.com/",
                "description": f"Free workout videos and plans for {skill_clean}",
                "resource_type": "video",
                "quality_score": 88
            })
    
    # Always add WikiHow for practical skills (it has guides for almost everything)
    resources.append({
        "title": f"WikiHow - {skill_clean} Guide",
        "url": f"https://www.wikihow.com/wikiHowTo?search={skill_url_safe}",
        "description": f"Step-by-step guides for {skill_clean}",
        "resource_type": "article",
        "quality_score": 80
    })
    
    # Add Reddit community if we don't have enough resources
    if len(resources) < 4:
        resources.append({
            "title": f"Reddit - {skill_clean} Community",
            "url": f"https://www.reddit.com/search/?q={skill_url_safe}",
            "description": f"Community discussions and resources for {skill_clean}",
            "resource_type": "article",
            "quality_score": 75
        })
    
    return resources[:4]  # Return top 4 resources

def get_fast_fallback_resources(skill_name):
    """Get immediate fallback resources without API calls"""
    normalized_skill = skill_name.strip()
    
    # Direct match first
    if normalized_skill in FAST_FALLBACK_RESOURCES:
        return FAST_FALLBACK_RESOURCES[normalized_skill]
    
    # Try case-insensitive matching
    for key in FAST_FALLBACK_RESOURCES:
        if key.lower() == normalized_skill.lower():
            return FAST_FALLBACK_RESOURCES[key]
    
    # Try partial matching for common variations
    normalized_lower = normalized_skill.lower()
    
    # Data Science subskills
    if 'data science fundamentals' in normalized_lower:
        return FAST_FALLBACK_RESOURCES.get('Data Science Fundamentals', [])
    elif 'intermediate data science' in normalized_lower:
        return FAST_FALLBACK_RESOURCES.get('Intermediate Data Science', [])
    elif 'practical data science' in normalized_lower:
        return FAST_FALLBACK_RESOURCES.get('Practical Data Science', [])
    elif 'advanced data science' in normalized_lower:
        return FAST_FALLBACK_RESOURCES.get('Advanced Data Science', [])
    elif 'data science best practices' in normalized_lower:
        return FAST_FALLBACK_RESOURCES.get('Data Science Best Practices', [])
    elif 'data science' in normalized_lower:
        return FAST_FALLBACK_RESOURCES.get('Data Science', [])
    
    # Python subskills
    elif 'python basics' in normalized_lower:
        return FAST_FALLBACK_RESOURCES.get('Python Basics', [])
    elif 'control structures' in normalized_lower or 'loops' in normalized_lower or 'if else' in normalized_lower:
        return FAST_FALLBACK_RESOURCES.get('Control Structures', [])
    elif 'functions' in normalized_lower and 'python' in normalized_lower:
        return FAST_FALLBACK_RESOURCES.get('Functions', [])
    elif 'object-oriented' in normalized_lower or 'oop' in normalized_lower or 'classes' in normalized_lower:
        return FAST_FALLBACK_RESOURCES.get('Object-Oriented Programming', [])
    elif 'python' in normalized_lower:
        return FAST_FALLBACK_RESOURCES.get('Python', [])
    
    # JavaScript subskills
    elif 'javascript fundamentals' in normalized_lower:
        return FAST_FALLBACK_RESOURCES.get('JavaScript Fundamentals', [])
    elif 'dom manipulation' in normalized_lower or 'dom' in normalized_lower:
        return FAST_FALLBACK_RESOURCES.get('DOM Manipulation', [])
    elif 'asynchronous javascript' in normalized_lower or 'async' in normalized_lower or 'promises' in normalized_lower:
        return FAST_FALLBACK_RESOURCES.get('Asynchronous JavaScript', [])
    elif 'javascript' in normalized_lower or 'js' in normalized_lower:
        return FAST_FALLBACK_RESOURCES.get('JavaScript', [])
    elif 'react' in normalized_lower:
        return FAST_FALLBACK_RESOURCES.get('React', [])
    elif 'html' in normalized_lower:
        return FAST_FALLBACK_RESOURCES.get('HTML', [])
    elif 'css' in normalized_lower:
        return FAST_FALLBACK_RESOURCES.get('CSS', [])
    elif 'machine learning' in normalized_lower or 'ml' in normalized_lower:
        return FAST_FALLBACK_RESOURCES.get('Machine Learning', [])
    elif 'data structure and algorithm' in normalized_lower or 'data structures and algorithms' in normalized_lower or normalized_lower == 'dsa':
        return FAST_FALLBACK_RESOURCES.get('Data Structures', [])
    elif 'data structure' in normalized_lower and len(normalized_lower.split()) <= 3:  # Only for main data structure searches
        return FAST_FALLBACK_RESOURCES.get('Data Structures', [])
    elif 'node' in normalized_lower or 'nodejs' in normalized_lower:
        return FAST_FALLBACK_RESOURCES.get('Node.js', [])
    elif 'git' in normalized_lower:
        return FAST_FALLBACK_RESOURCES.get('Git', [])
    elif 'sql' in normalized_lower or 'database' in normalized_lower:
        return FAST_FALLBACK_RESOURCES.get('SQL', [])
    elif 'algorithm' in normalized_lower and len(normalized_lower.split()) <= 2:  # Only for main algorithm searches
        return FAST_FALLBACK_RESOURCES.get('Algorithms', [])
    elif 'web development' in normalized_lower:
        # Return a mix of HTML, CSS, JavaScript for web development
        html_resources = FAST_FALLBACK_RESOURCES.get('HTML', [])[:2]
        css_resources = FAST_FALLBACK_RESOURCES.get('CSS', [])[:2]
        js_resources = FAST_FALLBACK_RESOURCES.get('JavaScript', [])[:2]
        return html_resources + css_resources + js_resources
    
    # If no specific match found, generate universal resources
    return generate_universal_resources(skill_name)
