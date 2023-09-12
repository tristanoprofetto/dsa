""""
BST Traversal - Medium

Write three function that take in a Binary Search Tree and empty array, and add its node's value with the following methods:
* In-Order Traversal
* Pre-Order Traversal
* Post-Order Traversal

Optimal time complexity: O(n)
Optimal space complexity: O(n)
"""

def in_order(tree, array):
    if tree is not None:
        in_order(tree.left, array)
        array.append(tree.value)
        in_order(tree.right, array)

    return array


def pre_order(tree, array):
    if tree is not None:
        array.append(tree.value)
        pre_order(tree.left, array)
        pre_order(tree.right, array)

    return array


def post_order(tree, array):
    if tree is not None:
        post_order(tree.left, array)
        post_order(tree.right, array)
        array.append(tree.value)

    return array