""""
BST Construction - Medium

Write a class for a Binary Search Tree supporting the following methods:
* insert values: inserts value in BST
* search for value: returns a boolean for whether a value exists in the BST
* remove value: finds the value to remove and adjusts the tree appropriately


Optimal Time Complexity: O(logN)
Optimal Space Complexity: O(n)
"""

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value, prev=None):
        current = self
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = BST(value)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = BST(value)
                    break
                else:
                    current = current.right
        return self

    
    def contains(self, value, parent = None):
        current = self
        while current is not None:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True
        return False
        

    def remove(self, value, parent = None):
        current = self
        while current is not None:
            if value < current.value:
                parent = current
                current = current.left
            elif value > current.value:
                parent = current
                current = current.right
            else:
                # found value to remove
                if current.left is not None and current.right is not None:
                    current.value = current.right.get_min()
                    current.right.remove(current.value, current)
                elif parent is None:
                    # for removing root node with children
                    if current.left is not None:
                        current.value = current.left.value
                        current.right = current.left.right
                        current.left = current.left.left
                    elif current.right is not None:
                        current.value = current.right.value
                        current.left = current.right.left
                        current.right = current.right.right
                    else:
                        # remove a root node without children nodes
                        pass
                elif parent.left == current:
                    parent.left = current.left if current.left is not None else current.right
                elif parent.right == current:
                    parent.right = current.left if current.left is not None else current.right
                break
                
        return self


    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.value


