

def gcdIter(a, b):
    number = min(a, b)

    while number > 0:
        if a % number == 0 and b % number == 0:
            return number
        number -= 1

def gcdRecur(a, b):
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)