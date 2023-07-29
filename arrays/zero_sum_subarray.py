# Zero Sum Subarray - Medium
# Write a function that takes in an array of integeres and returns a boolean whether theres exists a subarray of that sums to zero

def zero_sum_subarray(array):
    current = 0
    sums = set([0])
    for num in array:
        current += num
        if current in sums:
            return True
        sums.add(current)
    return False

# Optimal Time Complexity: O(n)
# Optimal Space Complexity: O(n)

if __name__ == "__main__":
    array = [-5, -5, 2, 3, -2]
    zero_sum_subarray(array)