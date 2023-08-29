""""
Branch Sums - Easy

Write a function that accepts a Binary Tree and returns a list of its branch sums ordered from left to right


Optimal Time Complexity: O(n)
Optimal Space Complexity: O(n)

sample input: 2
            /   \
           4     9
          /       \
         6         12
                  /  \
                11    20

output: [12, 34, 43]
"""

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branch_sums(root):
    pass


if __name__ == "__main__":
    tree = BinaryTree()
    branch_sums()