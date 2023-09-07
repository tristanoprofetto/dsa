"""
Binary Search - Easy

Write a function that takes in a sorted array of numbers and a target integer and implements binary search to return a boolean representing whether or not the target is in the array (otherwise return -1)


Optimal Runtime Complexity: O(log(N))
Optimal Space Complexity: O(1)
"""

def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        half = (left + right) // 2
        if array[half] == target:
            return half
        elif target < array[half]:
            right = half -1
        else:
            left = half + 1

    return -1
    

if __name__ == "__main__":
    array = [2, 4, 5, 8, 12, 14, 16, 19, 20, 28, 32, 54]
    target = 20

    binary_search(array, target)