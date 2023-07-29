# Knuth-Morris-Pratt Algorithm - Very Hard
# Given a string and substring return a boolean to represent whether or not the substring is actually a substring of the input string

def kmp_algorithm(string, substring):
    pattern = pattern_match(substring)
    return kmp_helper(string, substring, pattern)


def pattern_match(subtring):
    pattern = [-1 for i in substring]
    i = 0
    j = 1
    while i < len(subtring):
        if substring[i] == substring[j]:
            pattern[i] = j
            j += 1
            i += 1
        elif j > 0:
            j = pattern[j - 1] + 1
        else:
            i += 1
    return pattern


def kmp_helper(string, substring, pattern):
    i = 0
    j = 0
    while i + len(substring) - j <= len(string):
        if string[i] == substring[j]:
            if j == len(substring) - 1:
                return True
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j-1] + 1
        else:
            i += 1
    return False

# Optimal Time Complexity: O(n+m)
# Optimal Space Complexity:

if __name__ == "__main__":
    string = "fweojokiegojognijokesoifneokesi"
    substring = "jokes"
    kmp_algorithm(string, substring)