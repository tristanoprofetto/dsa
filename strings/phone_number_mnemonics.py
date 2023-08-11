"""
Phone Number Mnemonics - Medium

Write a function that takes in a string of numbers and returns all the possible combinations of phone number mnemonics...
only numbers 2-9 map to a list of letters while 0, and 1 remain digits..
similar to a phone keypad the mapping should resemble the following:
{
    1: 1,
    2: abc:
    3: def,
    4: ghi,
    5: jkl,
    6: mno,
    7: pqrs,
    8: tuv,
    9: wxyz,
    0: 0
}
the result should be a list of all the possible mnemonics that can be made


Optimal Time Complexity: O( 4^ n*n )
Optimal Space Complexity: O( 4 ^ n )

****
n: length of input digits
"""
map = {
    '1': '1',
    '2': "abc", 
    '3': "def", 
    '4': "ghi", 
    '5': "jkl", 
    '6': "mno", 
    '7': "pqrs", 
    '8': "tuv", 
    '9': "wxyz",
    '0': '0'
    }
# Recursive Solution
def phone_number_mnemonics(digits, map):
    current = ["0"] * len(digits)
    mnemonics = []
    helper(0, digits, current, mnemonics, map)
    return mnemonics

def helper(idx, digits, current, mnemonics, map):
    if idx == len(digits):
        mnemonic = ''.join(current)
        mnemonic.append(mnemonic)
    else:
        digit = digits[idx]
        letters = map[digit]
        for letter in letters:
            current[idx] = letter
            helper(idx + 1, digits, current, mnemonics, map)

# Iterative Solution
def phone_number_mnemonic(digits, map):
    mnemonics = [""]
    for number in digits:
        letters = map[number]
        current = []
        for letter in letters:
            for val in mnemonics:
                current.append(val + letter)
        mnemonics = current
    
    return mnemonics