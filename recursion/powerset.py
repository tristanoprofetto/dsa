"""
Powerset - Medium

Write a function that accepts an non-empty array of distinct integers and returns its powerset..
Powerset P(X) is defined as: [1, 2] ----> [[], [1], [2], [1, 2]]


Optimal Time Complexity: O(2 ** n)
Optimal Space Complexity: O(2 ** n)
"""

# Recursive solution
def powerset(array):
    power = [[]]
    if len(array) == 1:
        power.append(array)
        return power
    for i in range(len(array)):
        for element in powerset(array[:i] + array[i+1:]):
            output = sorted([array[i]] + element)
            if output not in power:
                power.append(output)
    return power

# Iterative solution
# def powerset(array):
#     power = [[]]
#     for num in array:
#         for i in range(len(power)):
#             power.append(power[i] + [num])

#     return power

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    powerset(array)