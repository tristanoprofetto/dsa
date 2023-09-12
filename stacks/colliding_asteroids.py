"""
Colliding Asteroids - Medium

Write a function that accepts an array of integers representing the direction and size of an asteroid, and returns the resulting array.
Asteroids move at the same speed therefore the only way for them to collide is if adjacent asteroids in the list are  moving toward eachother.
Positive sign: asteroid is moving to the right
Negaive sign: asteroid is moving to the left


Optimal Runtime Complexity: O(n)
Optimal Space Complexity: O(n)
"""

def colliding_asteroids(asteroids):
    stack = []
    for asteroid in asteroids:
        if asteroid > 0 or not stack:
            stack.append(asteroid)
        else:
            while stack and stack[-1] > 0:
                if stack[-1] == abs(asteroid):
                    stack.pop()
                    break
                elif stack[-1] > abs(asteroid):
                    break
                else:
                    stack.pop()
            else:
                stack.append(asteroid)

    return stack    


if __name__ == "__main__":
    asteroids = []
    colliding_asteroids(asteroids)