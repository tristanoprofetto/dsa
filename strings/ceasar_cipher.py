"""
Ceasar Cipher Encrypter - Easy

Write a function that takes a string and an integer and returns a new string where each letter in the string is shifted by k-spaces with respect to the alphabet


Optimal time complexity: O(n)
Optimal space complexity: O(n)
"""

def ceasar_cipher_encryptor(string, k):
    letters = "abcdefghijklmnopqrstuvwxyz"
    output =[]
    for c in string:
        idx = string.index(c)
        if idx + k >= 26:
            new_idx = (idx + k) % 26
        else:
            new_idx = idx + k
        output.append(letters[new_idx])
    
    return ''.join(output)
        

if __name__ == "__main__":
    string = "fidsnogindsiogdgsauisba"
    k = 10
    ceasar_cipher_encryptor(string, k)