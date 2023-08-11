"""
Anagrams - Medium

Write a functiion that accepts an array of strings and groups anagrams together

Optimal Time Complexity: O( w * n * log(N) )
Optimal Space Complexity: O(wn)

******
w: # words
n: lenth of the longest word
"""

def group_anagrams(words):
    anagrams = {}
    for word in words:
        # Sort word alphabetically
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    return list(anagrams.values())


if __name__ == "__main__":
    words = ['good', 'cat', 'act', 'odog', 'god', 'dog', 'rat', 'tar', 'king']
    group_anagrams(words)
