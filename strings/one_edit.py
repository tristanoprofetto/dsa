"""
One Edit - Medium

Write a function that takes two strings (s1, s2) and determines if the two can be made equal using only ONE edit
An edit can be one of the following operations:
* add: one character can be added to a given index
* remove: one character can be removed at a given index
* replace: one character can be swapped for another character at a given index

Optimal time complexity: O(n)
Optimal space complexity: O(1)
"""

def one_edit_strings(s1, s2):
    l1, l2 = len(s1), len(s2)
    if abs(l1 - l2 ) > 1:
        return False
    edits = 0
    i = 0
    j = 0
    while i < l1 and j < l2:
        if s1[i] != s2[j]:
            if edits > 0:
                return False
            edits += 1
            if l1 > l2:
                i += 1
            elif l1 < l2:
                j += 1
            else:
                i += 1
                j += 1
        else:
            i += 1
            j += 1
    return True


if __name__ == "__main__":
    s1 = "whazsup"
    s2 = "whatsup"
    one_edit_strings(s1, s2)