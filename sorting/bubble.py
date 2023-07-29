# Bubble Sort - Easy
# Write a function that takes in an unordered array of integers and returns a sorted array
# The sorted array should be obtained by implementing the Bubble sort algorithm

def bubble_sort(array):
    is_sorted = False 
    while not is_sorted:
        is_sorted = True
        for i, j in zip(range(len(array) - 1), range(1, len(array))):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                is_sorted = False

    return array

# Optimal Time Complexity: O(n)
# Optimal Space Complexity: O(1)

if __name__ == "__main__":
    array = [8, 5, 2, 9, 5 ,7]
    bubble_sort(array)