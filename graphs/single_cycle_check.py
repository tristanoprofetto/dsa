"""
Single Cycle Check - Medium

Given an array of integers where each represents a jump of its value in the array, write a function which returns a boolean for whether or not a single cycle can be performed.
A single cycle occurs if starting at any index every element is visited exactly once before returning to the starting index...

Optimal Time Complexity: O()
Optimal Space Complexity: O()
"""

def single_cycle(array):
    seen = 0
    current_idx = 0
    while seen < len(array):
        current_idx += array[current_idx]
        current_idx %= len(array)
        seen += 1
        if current_idx == 0 or array[current_idx] == 0:
            break
    
    return seen == len(array) and current_idx == 0


if __name__ == "__main__":
    array = [2, 3, 1, -4, -4, 2]
    single_cycle(array)