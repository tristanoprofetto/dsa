"""
Min Height BST - Medium

Write a function that takes a non-empty array of sorted integers and constructs a BST with minimum height


Optimal time complexity: O(n)
Optimal space complexity: O(n)
"""

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


def min_height(array):
    return helper(array, 0, len(array) - 1)


def helper(array, start, end):
    if end < start:
        return None
    mid = (start + end) // 2
    tree = BST(array[mid])
    tree.left = helper(array, start, mid - 1)
    tree.right = helper(array, mid + 1, end)
    return tree
        