"""
Validate BST -  Medium

Write a funciton that takes in a tree and returns a boolean representing whether or not it is a valid BST

Optimal time complexity: O(n) (n is the number of nodes)
Optimal space complexity: O(d) (d is the depth of the tree)
"""

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    
def validate_bst(tree, left_parent = None, right_parent = None):
    if tree is None:
        return True
    elif left_parent is not None and left_parent.value >= tree.value:
        return False
    elif right_parent is not None and right_parent.value < tree.value:
        return False
    
    return validate_bst(tree.left, tree, right_parent) and validate_bst(tree.right, left_parent, tree)