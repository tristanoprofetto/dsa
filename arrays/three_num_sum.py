# Write a function that takes in a non-empty array of distinct integers and a target
# The function should return all triplets of integers that sum to the input target

def three_number_sum(array, target):
    trips = []
    for i in range(len(array)):
        left = 0
        right = len(array) - 1
        while left < right and left != array[i] and right != array[i]:
            if array[i] + array[left] + array[right] == target:
                trips.append([array[i], array[left], array[right]])
            left += 1
            right -= 1
    return trips
