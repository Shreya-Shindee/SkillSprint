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
            "resource_type": "tutorial",
            "quality_score": 88
        },
        {
            "title": "Array Data Structure - MDN Documentation",
            "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array",
            "description": "Complete JavaScript Array documentation with examples",
            "resource_type": "documentation",
            "quality_score": 95
        },
        {
            "title": "Array Algorithms Tutorial - YouTube",
            "url": "https://www.youtube.com/watch?v=QJNwK2uJyGs",
            "description": "Comprehensive video tutorial on array algorithms and techniques",
            "resource_type": "video",
            "quality_score": 87
        },
        {
            "title": "Awesome Array Algorithms - GitHub",
            "url": "https://github.com/TheAlgorithms/Python/tree/master/data_structures/arrays",
            "description": "Collection of array algorithm implementations in Python",
            "resource_type": "github",
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
            "title": "Linked List Problems - LeetCode",
            "url": "https://leetcode.com/tag/linked-list/",
            "description": "Practice linked list problems with step-by-step solutions",
            "resource_type": "course",
            "quality_score": 88
        },
        {
            "title": "Linked List Visualization",
            "url": "https://www.cs.usfca.edu/~galles/visualization/LinkedList.html",
            "description": "Interactive linked list operations visualization",
            "resource_type": "tutorial",
            "quality_score": 90
        },
        {
            "title": "Linked Lists - CS50 Documentation",
            "url": "https://cs50.harvard.edu/x/2023/notes/5/",
            "description": "Harvard CS50 comprehensive notes on linked lists",
            "resource_type": "documentation",
            "quality_score": 94
        },
        {
            "title": "Linked List Masterclass - YouTube",
            "url": "https://www.youtube.com/watch?v=WwfhLC16bis",
            "description": "Complete linked list tutorial with coding examples",
            "resource_type": "video",
            "quality_score": 86
        },
        {
            "title": "Linked List Implementations - GitHub",
            "url": "https://github.com/TheAlgorithms/Python/tree/master/data_structures/linked_list",
            "description": "Various linked list implementations and algorithms",
            "resource_type": "github",
            "quality_score": 84
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
            "title": "Binary Tree Problems - LeetCode",
            "url": "https://leetcode.com/tag/binary-tree/",
            "description": "Practice binary tree problems with solutions",
            "resource_type": "course",
            "quality_score": 89
        },
        {
            "title": "Tree Traversal Visualization",
            "url": "https://www.cs.usfca.edu/~galles/visualization/BinTree.html",
            "description": "Interactive binary tree traversal visualization",
            "resource_type": "tutorial",
            "quality_score": 88
        },
        {
            "title": "Trees - Algorithm Design Manual",
            "url": "https://www3.cs.stonybrook.edu/~skiena/214/lectures/lect10/lect10.html",
            "description": "Academic documentation on tree data structures",
            "resource_type": "documentation",
            "quality_score": 93
        },
        {
            "title": "Binary Trees Explained - YouTube",
            "url": "https://www.youtube.com/watch?v=H5JubkIy_p8",
            "description": "Visual explanation of binary trees and operations",
            "resource_type": "video",
            "quality_score": 85
        },
        {
            "title": "Binary Tree Algorithms - GitHub",
            "url": "https://github.com/TheAlgorithms/Python/tree/master/data_structures/binary_tree",
            "description": "Binary tree algorithm implementations",
            "resource_type": "github",
            "quality_score": 83
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
            "description": "Learn shortest path algorithms like Dijkstra and Floyd-Warshall",
            "resource_type": "article",
            "quality_score": 85
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
