def max_val(t):
    """ t, tuple
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    maxVal = 0
    for element in t:
        if isinstance(element, int):
            if element > maxVal:
                maxVal = element
        elif max_val(element) > maxVal:
            maxVal = max_val(element)

    return maxVal

t = (5, (1,2), [[1],[2]])

if max_val(t) == 5:
    print("Passed")
else:
    print("Failed, max is:" + str(max_val(t)))


t = (5, (1,2), [[1],[9]])

if max_val(t) == 9:
    print("Passed")
else:
    print("Failed, max is:" + str(max_val(t)))
