"""
Nearest Exit from Entrance in Maze - Medium

You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') adn walls represented as '+'. You are also given the entrance of the maze, where entrance = [entrance_row, entrance_col] denotes the row and column of the cell you are initially standing at.
In one step you can move up, down, left, or right from and to an empty cell in the maze. You cannot move through walls. 
Return the number of steps needed to reach the exit from the entrance. If there is no exit, return -1.

Optimal time complexity: O(mn)
Optimal space complexity: O(mn)
"""
import collections


def nearest_exit(maze, entrance):
    rows, cols = len(maze), len(maze[0])
    q = collections.deque([(entrance[0], entrance[1], 0)])
    maze[entrance[0]][entrance[1]] = '+'
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while q:
        row, col, steps = q.popleft()
        if row == 0 or row == rows -1 or col == 0 or col == cols -1:
            return steps
        for dx, dy in directions:
            x, y = row + dx, col + dy
            if 0 <= x < rows and 0 <= y < cols and maze[x][y] == '.':
                maze[x][y] = '+'
                q.append((x, y, steps + 1))
    
    return -1


if __name__ == "__main__":
    maze = [['+', '+', '+', '+', '+', '+'], 
            ['+', '.', '.', '.', '.', '+'], 
            ['+', '.', '+', '+', '.', '+'], 
            ['+', '.', '.', '.', '.', '+'], 
            ['+', '+', '+', '+', '+', '+']]
    entrance = [1, 2]
    print(nearest_exit(maze, entrance))