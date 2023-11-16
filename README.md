# Data Structures and Algorithms in Python
The following repository provides solutions for DSA problems ranging from easy to very hard...

## Analyzing Data Structures and Algorithms
* Complexity Analysis: the process of determining how efficient an algorithm is with respect to the time it takes to run the program or how much memory space is used per unit of input.
* Time Complexity: measures how fast an algorithm runs 
* Space Complexity: measures how much auxilary memory is used when running an algorithm.
* Big O notations from fastest to slowest (n is the number of inpput elements):
* * Constant: O(1)
* * Linear: O(n)
* * Logarithmic: O(logN)
* * Log-Linear: O(n*logN)
* * Quadratic: O(n<sup>2</sup>)
* * Cubic: O(n<sup>3</sup>)
* * Exponential: O(2<sup>n</sup>)
* * Factorial: O(n!)

![chart](https://i.ytimg.com/vi/47GRtdHOKMg/maxresdefault.jpg)

### Memory
* Bit: a binary digit (0 or 1) represents a state
* Byte: a group of 8 bits, a single byte can represent up to 256 data points (2<sup>8</sup>)
* Bytes in memory can point to other bytes in memory as a store of reference

Here is some theory for some data structures
### Arrays
Arrays are a linear collection of data values acceessible through numbered indices (starting at 0)
There are two common types of arrays
1. static arrays: allocates a fixed amount of memory for storing values when initialized
2. dynamic arrays: allocates double the amount of memory needed for storing values when initialized
Time complexities of certain array operations:
* Accessing at a given index: O(1)
* Updating a value at a given index: O(1)
* Insertion: O(n)
* Deleting: O(n)
* Copying an array: O(n)


### Linked Lists
A structure that consists of nodes with a value and who point to next or previous node in the list depending on the type of linked lists
There are 4 common types of linked lists
1. Singly Linked List
2. Doubly Linked List
3. Circular Linked List
4. Doubly Circular Linked List

![linked-list](https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2013/03/Linkedlist.png)

### Stacks
Array-like structure whos elements follow LIFO (last in first out)
Stacks are typically implemented using dynamic arrays or linked-lists
Time complexities of certain stack operations:
* Pushing an element onto the stack: O(1)
* Popping an element from the stack: O(1)
* Searching for an element in the stack: O(n)

![stack](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20221219100314/stack.drawio2.png)

### Queues
Array-like structue whos elements follow FIFO
Queues are typically implemented using doubly linked lists
Time complexities of certain queue operations:
* Enqueuing an element: O(1)
* Dequeueing an element: O(1)
* Searching for an element: O(n)

![queue](https://media.geeksforgeeks.org/wp-content/uploads/20220805131014/fifo.png)

### Hash Tables
Provides fast insertion, deletion, and lookup of {key: value} pairs
Under the hood hash tables use a dynamic array of linked lists to efficiently store k/v pairs
Time complexities of certain hash table operations:
* Inserting k/v pair: O(1)
* Removing k/v pair: O(1)
* Lookup a key: O(1)


### Graphs
A collection of nodes (vertices) connected by edges (directed/undirected)
* Graph Cycle: when three or more vertices are connected
There are several types of graphs...

##### Acyclic Graph
A graph that has no cycles

##### Cyclic Graph
A graph that has atleast one cycle

##### Directed Graph
A graph whos edges are directed, these edges can only be traversed in one direction

##### Undirected Graph
A graph whose edges are undirected

There are two primary methods for traversing a graph:
* Depth-First Search (DFS): suitable for finding the longest path from the root node (use Queue)
* Breath-First Search (BFS): suitable for finding the shortest path to the starting node (use Stack)

![BFSDFS](https://open4tech.com/wp-content/uploads/2019/01/BFS-DFS.png)

### Trees
A directed graph structure that is rooted with child nodes.
A data structure that consists of nodes, each with a value and a point to a child node.
Recursively these forms subtrees in the given tree.
* Root Node: the first node in the tree
* Leaf Nodes: node without any child nodes
* Branches: the path from the root of a tree to a corresponding leaf

Methods for traversing trees:
* In-Order Traversal
* Pre-Order Traversal
* Post-Order Traversal

![traversals](https://media.geeksforgeeks.org/wp-content/uploads/20230623123129/traversal.png)

There are several types of trees in the context of data structures...

##### Binary Tree
A tree where each node has up to two child-nodes.
Many of its operations have logarithmic time complexity.

* Perfect Binary Tree: when every node has exactly two child-nodes, and all have the same depth
* Binary Search 

##### Binary Search Trees
A special case of binary trees where each left child node is less than its parent, and each right child node is strictly greater than or equal to its parent.

##### K-Ary Tree

##### Heaps
A specialized tree that is a complete binary tree which satisfies the heap properties.
Generally Heaps can be of two types:
1. Max-Heap: the root value must be greater than all its child-nodes
2. Min-Heap: root value but be smaller than all its child-nodes.

Operations on Heaps:
* Insertion: O(log N)
* Deletion: O(log N)

##### Tries
A type of k-ary search tree used for storing and searching a specific key from a set. 
Often used for storing strings over an alphabet, used in spell checking programs

Advantages of Tries:
1. In tries the keys are searched using common prefixes. Hence it is faster. The lookup of keys depends upon the height in case of binary search tree. 
2. Tries take less space when they contain a large number of short strings. As nodes are shared between the keys.
3. Tries help with longest prefix matching, when we want to find the key.


