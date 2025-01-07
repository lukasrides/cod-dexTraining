


def checkPalindrome():
    text = input("Enter a text: ")
    text = text.lower()
    charList = list(text)
    # rentner = 0-6
    palindrome = False

    for i in range(len(charList)):
        if charList[i] == charList[-(i+1)]:
            palindrome = True
        else:
            return False
    return palindrome       


isPalindrome = checkPalindrome()
if isPalindrome:
    print('Input is a palindrome!')
else:
    print('Input is no palindrome!')