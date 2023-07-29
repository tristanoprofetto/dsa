# Missing Numbers
# You're given an unordered list of unique integers nums in the range [1, n] where n represents the length of nums + 2
# Write a function that takes in this listr and returns a new list with the two missing numbers sorted from lowest to highest

def missing_numbers(nums):
    return [i for i in range(1, len(nums) + 3) if i not in nums]


# Optimal Time Complexity: O(n)
# Optimal Space Complexity: O(1)

if __name__ == "__main__":
    nums = [1, 3 ,5 ,6, 7]
    missing_numbers(nums)