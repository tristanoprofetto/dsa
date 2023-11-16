""""
Three Number Sum - Medium

Write a function that takes an array of integers and returns all the possible triplets that sum to the target.


Optimal time comlexity: O(n ** 2)
Optimal space complexity: O(n)
"""

def three_number_sum(array, target):
    trips = []
    array.sort()
    for i in range(len(array)):
        left = i + 1
        right = len(array) - 1
        while left < right:
            if array[i] + array[left] + array[right] == target:
                trips.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif array[i] + array[left] + array[right] < target:
                left += 1
            else:
                right -= 1
    return trips

if __name__ == "__main__":
    array = [-1, -3, 4, 5, 7, 3, 4, 7, 3, 0, -2]
    target = 5
    three_number_sum(array, target)
