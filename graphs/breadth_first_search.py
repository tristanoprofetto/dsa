"""
Breadth-First Search - Medium

Given a Node class implement the breadth-first search method on the Node class. 
Return the node values in an array

Optimal time complexity: O(v + e)
Optimal space complexity: O(v)

* v: number of vertices
* e: number of edges
"""

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def bfs(self, array):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)

