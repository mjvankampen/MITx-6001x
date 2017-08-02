
def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    total = 0
    n = 1
    while total < k:
        total += n
        n += 1

    if total == k:
        return True
    else:
        return False

numbers = [1,3, 6, 10, 15, 16]
for k in numbers:
    print('Number: ' + str(k) + ' triangular: ' + str(is_triangular(k)))