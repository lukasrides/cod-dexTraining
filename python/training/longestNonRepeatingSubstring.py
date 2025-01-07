
# abcabcbb
def longestNonRepeatingSubstring(s):

    currLength = 0
    maxLength = 0
    tempList = list()

    for char in s:
        if not char in tempList:
            tempList.append(char)
            currLength += 1
        else:
            if currLength > maxLength:
                maxLength = currLength
            currLength = 0
            tempList.clear()
            tempList.append(char)
            currLength += 1
    
    if currLength > maxLength:
                maxLength = currLength
    

    return maxLength


print(longestNonRepeatingSubstring('abcabcbb')) # Output: 3 ("abc")
print(longestNonRepeatingSubstring('bbbbb')) # Output: 1 ("b")
print(longestNonRepeatingSubstring('pwwkew')) # Output: 3 ("wke")
print(longestNonRepeatingSubstring('')) # Output: 0
print(longestNonRepeatingSubstring('au')) # Output: 2 ("au")