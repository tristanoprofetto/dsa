"""
Youngest Common Ancestor - Medium

Write a function that accepts the Ancestor class representing a graph that traverses upwards when calling the ancestor method.
Given two seperate nodes as input return the youngest common ancestor between the two...


Optimal time complexity: O(d) (d is the depth of the tree)
Optimal space complexity: O(1)
"""

class Ancestor:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def youngest_common_ancestor(descendant_a, descendant_b):
    ones, twos = {}, {}
    one, two = descendant_a, descendant_b
    while True:
        if one is not None and two is not None:
            if one is not None:
                if one.name in twos.keys():
                    return one
                ones[one.name] = one
                one = one.ancestor

            if two is not None:
                if two.name in ones.keys():
                    return two
                twos[two.name] = two
                two = two.ancestor

            if one is None or two is None:
                continue
        else:
            break
    pass