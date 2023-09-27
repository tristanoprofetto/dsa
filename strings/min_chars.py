"""
Minimum Characters for Words - Medium


Write a function that takes an array of words, and returns the minimum array of characters required for constructing all the words in the array.


Optimal time complexity: O(n * m) 
Optimal space complexity: O(u)

Where:
* n is the number of words
* m is the length of the longest word
* u is the number of unique characters
"""

def min_chars_for_words(words):
    char_counts = []
    for word in words:
        counts = {}
        for char in word:
            if char in map:
                counts[char] += 1
            else:
                counts[char] = 1
        char_counts.append(counts)

    flattened = {}
    for i in range(len(char_counts)):
        for k, v in zip(char_counts[i].keys(), char_counts[i].values()):
            if k in flattened:
                flattened[k] = max(flattened[k], v)
            else:
                flattened.update({k: v})

    result = []
    for k, v in zip(flattened.keys(), flattened.values()):
        while v > 0:
            result.append(k)
            v -= 1

    return result


if __name__ == "__main__":
    words = []
    min_chars_for_words(words)