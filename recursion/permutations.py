"""
Permutations - Medium

Write a function that accepts an array of random integers and returns all the possible permutations of them..
ex: array = [1, 2, 3] ----> [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]


Time Complexity: O(n* n!)
Space Complexity: O(n*n!)
"""

def permutations(array):
    perms = []
    if len(array) == 1:
        return [array]
    for i in range(len(array)):
        for element in permutations(array[i:] + array[i+1:]):
            perms.append([array[i]] + element)

    return perms


if __name__ == "__main__":
    array = [1, 2, 3, 4]
    permutations(array)