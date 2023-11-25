"""
Keys and Rooms - Medium

There are N rooms and you start in room 0. Your goal is to visit every room, but you can't enter a loicked room without having its key.
Each room may have one or more keys to access the next room.  Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in
Given a list of rooms, each room rooms[i] contains keys rooms[i][j], start in

Optimal time complexity: O(n)
Optimal space complexity: O(n)
"""

def visit_all_rooms(rooms):
    visited = set()
    stack = [0]
    while stack:
        room = stack.pop()
        if room not in visited:
            visited.add(room)
            stack.extend(rooms[room])
    return len(visited) == len(rooms)


if __name__ == "__main__":
    rooms = [[1,3],[3,0,1],[2],[0]]
    print(visit_all_rooms(rooms))
    rooms = [[1],[2],[3],[]]
    print(visit_all_rooms(rooms))