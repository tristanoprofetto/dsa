"""
Successful Pairs of Spells and Potions - Medium

You are given two arrays spells and potions where each position in the arrays represents a spell or potion of that stength with an integer value.
You are also given an integer success representing the minimum total strength required for a successful pairing of a spell and a potion.
A successful pairing is one where the strength of the spell and potion add up to at least the minimum strength.
Return the number of successful pairings.

ex: spells = [2, 4, 5], potions = [4, 6, 7, 8, 9], success = 10

pairs = [1, 5, 5]


Optimal time complexity: O(Nlogn)
Optimal spcace complexity: O(n)
"""

def successful_pairs(spells: list, potions: list, success: int):
    spells.sort()
    result = []
    for spell in spells:
        l, r = 0, len(potions) - 1
        count = 0
        while l <= r:
            mid = (l + r) // 2
            if potions[mid] * spell >= success:
                count = r - mid + 1
                r = mid - 1
            else:
                l = mid + 1
        result.append(count)
    
    return result
    

if __name__ == "__main__":
    spells = [2, 4, 5, 8, 10]
    potions = [4, 6, 7, 8, 9]
    success = 10
    print(successful_pairs(spells, potions, success))