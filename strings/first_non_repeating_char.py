"""
First Non-Repeating Character - Easy

Write a function that accepts a string and returns the first non-repeating character...
If all characters repeat the function should return -1

Optimal Time Complexity: O(n)
Optimal Space Complexity: O(1)
"""

def first_non_repeating(string):
    map = {}
    for c in range(len(string)):
        if string[c] in map:
            map[string[c]]['count'] += 1
        else:
            map[string[c]] = {'idx': c, 'count': 1}

    for v in map.values():
        if v['count'] == 1:
            return v['idx']
        
    return -1


if __name__ == "__main__":
    string = "fuefhneiuhuigeg"
    first_non_repeating(string)