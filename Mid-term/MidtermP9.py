def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    '''
    greatest = 0

    if not L1 and not L2:
        return (None, None, None)
    elif not L1 or not L2:
        return False
    elif len(L1) != len(L2):
        return False

    for item in L1:
        if L1.count(item) != L2.count(item):
            return False
        else:
            if L1.count(item) > greatest:
                greatest = L1.count(item)
                element = item
                elementType = type(item)

    return (element, greatest, elementType)

L1 = ['a', 'a', 'b']
L2 = ['a', 'b']
print(is_list_permutation(L1, L2))

L1 = [1, 'b', 1, 'c', 'c', 1]
L2 = ['c', 1, 'b', 1, 1, 'c']
print(is_list_permutation(L1, L2))