def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    """

    if aStr == '' or len(aStr) // 2 == 0:
        return False
    elif char == aStr[len(aStr) // 2]:
        return True
    elif char < aStr[len(aStr) // 2]:
        return isIn(char, aStr[:(len(aStr) // 2)])
    else:
        return isIn(char, aStr[(len(aStr) // 2):])

print(isIn('a','abcd'))
