""""
Min Max Stack - Medium

Write a Min Max Stack that supports the following operations:
* pushing value
* popping value
* peek value atop the stack
* retrieve min and max element from the stack


Required Time Complexity: O(1)
Required Space Complexity: O(1)
"""

class Stack:
    def __init__(self):
        self.stack = []

    def peek(self):
        return self.stack[-1]

    def pop(self):
        return self.stack.pop()
    
    def push(self, value):
        self.stack.append(value)
        
    def get_min(self):
        return min(self.stack)

    def get_max(self):
        return max(self.stack)
    

if __name__ == "__main__":
    stack = Stack()