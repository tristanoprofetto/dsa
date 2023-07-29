# Three Largest Numbers - Easy
# Given a list of integers return a list of the three largest integers in ascending order

def three_largest(array):
    largest = []
    for _ in range(3):
        largest.append(max(array))
        array.remove(max(array))
        
    return largest[::-1]

# Optimal Time Complexity: O(n)
# Optimal Space Complexity: O(1)

if __name__ == "__main__":
    array = []
    three_largest()