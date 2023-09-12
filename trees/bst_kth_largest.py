""""
Find Kth Largest Value in BST - Medium

Write a function that takes in a Binary Search Tree and a positive integer k and returns the kth largest node value in the tree.


Optimal time complexity: O(h + k) (k is input param)
Optimal space complexity: O(h) (h is height of tree)
"""

class BST:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = None
        self.right = None

# Recursive solution (reverse pre-order)
def kth_largest(tree, k):
    pass

# Iterative solution
def kth_largest(tree, k):
    count = 1
    current = tree
    stack = []
    while current or stack:
        if current:
            stack.append(current)
            current = current.right
        else:
            current = stack.pop()
            if count == k:
                return current.value
            count += 1
            current = current.left