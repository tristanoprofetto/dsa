"""
Insertion Sort - Easy

Write a function that takes in an unordered array of integers and returns a sorted array
The sorted array should be obtained by implementing the insertion sort algorithm

Optimal Time Complexity: O(n)
Optimal Space Complexity: O(1)
"""

def insertion_sort(array):
    result = [array[0]]
    for i in range(1, len(array)):
        j = i-1
        if array[i] > result[j]:
            result.append(array[i])
        else:
            while array[i] < result[j] and j >= 0:
                j -= 1
            result.insert(j+1, array[i])
    return result



if __name__ == "__main__":
    array = []
    insertion_sort(array)