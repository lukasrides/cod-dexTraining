"""
Write a function first_non_repeating_char(s: str) -> str that takes a string s as input and returns the first non-repeating character. 
If there is no non-repeating character, return an empty string "".
"""

def firstNonRepeatingChar(s):
    charList = list(s)
    charDict = dict().fromkeys(charList)

    # store dict with count of occurrences
    for key in charDict:
        charDict[key] = charList.count(key)

    # iterate over input string, first occurrence with count=1 is the return value
    for char in charList:
        if charDict[char] == 1:
            return char
    return ''


def firstNonRepeatingCharOptimized(s):
    # Create a dictionary to count occurrences
    charDict = {}
    
    # First pass: count the occurrences of each character
    for char in s:
        charDict[char] = charDict.get(char,0) + 1
    
    # Second pass: find the first character with a count of 1
    for char in s:
        if charDict[char] == 1:
            return char
    return ''




print('First single char: ', firstNonRepeatingChar('abacabad'.lower()))
print('First single char: ', firstNonRepeatingChar('aabbcc'.lower()))
print('First single char: ', firstNonRepeatingChar('zxcvbnm'.lower()))

print('First single char: ', firstNonRepeatingCharOptimized('abacabad'.lower()))
print('First single char: ', firstNonRepeatingCharOptimized('aabbcc'.lower()))
print('First single char: ', firstNonRepeatingCharOptimized('zxcvbnm'.lower()))
