def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """

    greatestOdd = -1
    for number in range(0, 11):
        count = L.count(number)
        if count % 2 != 0 and number > greatestOdd:
            greatestOdd = number

    if greatestOdd == -1:
        return None
    else:
        return greatestOdd
    