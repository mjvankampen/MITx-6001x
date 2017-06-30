from math import tan, pi


def polysum(n, s):
    """
    :rtype: float
    :param n: number of sides
    :param s: length of side
    :return: the area summed with the perimeter squared
    """

    area = 0.25 * n * s ** 2 / tan(pi / n)
    perimeter = n * s

    return round(area + perimeter ** 2, 4)
