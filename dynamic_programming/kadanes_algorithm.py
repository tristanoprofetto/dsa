"""
Kadanes Algorithm - Medium

Write a function that takes in a non-empty array of integers and returns the max sum from a subarray of the input array
Subarray sums can only be calculated for adjacent value


Optiomal Time Complexity: O(n)
Optimal Space Complexity: O(1)
"""

def kadanes_algorithm(array):
    current = float('-inf')
    running_sum = float('-inf')
    for num in array:
        running_sum = max(num, running_sum + num)
        current = max(current, running_sum)

    return current


if __name__ == "__main__":
    array = [3, 6, 7, -10, 3, 5, -2, 1]
    kadanes_algorithm(array)