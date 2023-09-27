"""
Best Digits - Medium

Write a function that takes a number (str) and the number of digits to remove from the string. 
Return the highest possible number that can be returned after removing the required number of digits.

Optimal time complexity: O(n)
Optimal space complexity: O(n)
"""

def max_number(number, digits):
    stack = []
    for num in number:
        while digits > 0 and len(stack) > 0 and num > stack[-1]:
            digits -= 1
            stack.pop()
        stack.append(num)

    return ''.join(stack[:len(stack) - digits])

if __name__ == "__main__":
    number = "438927498"
    digits = 3
    max_number(number, digits)