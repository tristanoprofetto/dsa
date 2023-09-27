"""
Depth-First Search - Easy

Given a Node class write the method that implements depth-first search.


Optimal time complexity: O()
Optimal space complexity: O()

"""

class Node:
    def __init___(self, name):
        self.name = name
        self.children = []

    def add_child(self, name):
        self.children.append(Node(name))
        return self

    def dfs_recursive(self, array):
        array.append(self.name)
        for child in self.chidlren:
            child.dfs_recursive(array)
        return array
    
    def dfs_iterative(self, array):
        stack = [self]
        while stack:
            top = stack.pop()
            array.append(top.name)
            stack.extend([child for child in top.children][::-1])
        
        return array
