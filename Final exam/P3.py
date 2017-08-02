def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    total = 0
    digits = False

    for char in s:
        if char.isdigit():
            total += int(char)
            digits = True
    if digits is False:
        raise ValueError('No characters found')
    return total

s = "a12ha3b"
if sum_digits(s) == 6:
    print("Passed")
else:
    print("Failed")

s = "a;35d4"
if sum_digits(s) == 12:
    print("Passed")
else:
    print("Failed")

s = "abc"
if sum_digits(s) == 12:
    catch
else:
    print("Failed")