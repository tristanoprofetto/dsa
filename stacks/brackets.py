""""
Balanced Brackets - Medium

Write a function that takes a string with the following chars
Brackets:
* ()
* []
* {}
Return a boolean representing whether or not the brackets are balanced...
*** Note brackets are balanced if there is a close bracket for every open brack, but a close bracket must come after its corresponding open bracket

Optimal time complexity: O(n)
Optimal space complexity: O(1)
"""

def balanced_brackets(string):
    stack = []
    open = "({["
    close = ")}]"
    map = {i: j for i, j in zip(close, open)}
    for c in string:
        if c in open:
            stack.append(c)
        elif c in close:
            if not stack:
                return False
            else:
                top = stack.pop()
                if top == map[c]:
                    continue
                else:
                    return False
        else:
            continue

    return True if not stack else False

if __name__ == "__main__":
    string = "([{}])[]{}"
    balanced_brackets()