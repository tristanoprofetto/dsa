# Given two input arrays of student heights, return whether or not it is possible to take a Class photo
# Two arrays represent students wearing blue shirts and students wearing red shirts
# The following conditions must all be met:
# 1. all students should be in the row corresponding to their shirt colors
# 2. each student in the back row must be TALLER than the student directly infront of him

def class_photos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    increasing = True
    decreasing = True
    for i in range(len(redShirtHeights)):
        if redShirtHeights[i] < blueShirtHeights[i]:
            decreasing = False
        if redShirtHeights[i] > blueShirtHeights[i]:
            increasing = False
        if redShirtHeights[i] == blueShirtHeights[i]:
            return False
        
    return increasing or decreasing

# Optimal Time Complexity: O(nlogN)
# Optimal Space Complexity: O(1)

if __name__ == "__main__":
    class_photos([5, 8, 1, 3, 4], [6, 9, 2, 4, 5])
