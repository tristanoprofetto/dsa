"""
Binary Tree Right Side View - Medium

Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Optimal time complexity: O(n)
Optimal space complexity: O(n)
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None


def right_side(root):
    if root is None:
        return []
    queue = [root]
    result = []
    while queue:
        right = None
        for i in range(len(queue)):
            node = queue.pop(0)
            if node is not None:
                right = node
                queue.append(node.left)
                queue.append(node.right)
        if right:
            result.append(right.val)
    
    return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)

    print(right_side(root))