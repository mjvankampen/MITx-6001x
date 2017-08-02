def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """

    def f(x):
        total = 0
        power = 0
        for num in reversed(L):
            total += num * x ** power
            power += 1
        return total

    return f

print(general_poly([1, 2, 3, 4])(10))