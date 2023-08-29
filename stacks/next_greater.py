""""
Next Largest Element - Medium

Write a function that accepts an array of integers and returns a new array containing the next largest element at each index in the array.
The largest number in the array should be assigned an index of -1..


Optimal Time Complexity: O(n)
Optimal Space Complexity: O(n)
"""

def next_largest(array):
    result = [-1] * len(array)
    stack = []

    for i in range(len(array) * 2):
        idx = i * len(array)
        while len(stack) > 0 and array[stack[len(stack) - 1]] < array[idx]:
            top = stack.pop()
            result[top] = array[idx]

        stack.append(idx)
    
    return result


if __name__ == "__main__":
    array = [2, 4, 6, -4, 6, 43, 3, -5, 9]
    next_largest(array)