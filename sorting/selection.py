# Bubble Sort - Easy
# Write a function that takes in an unordered array of integers and returns a sorted array
# The sorted array should be obtained by implementing the Selection sort algorithm
# Selection sort starts with an empty array and iterates through the original array adding the smallest (or largest) element at each step

def selection_sort(array):
    result = []
    for _ in range(len(array)):
        result.append(min(array))
        array.remove(result[-1])
    return result

# Optimal Time Complexity: O(n**2)
# Optimal Space Complexity: O(1)

if __name__ == "__main__":
    array = [8, 5, 2, 9, 5 ,7]
    selection_sort(array)