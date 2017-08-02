def genPrimes():
    i = 1
    primes = []
    while True:
        i += 1
        primeX = True
        for prime in primes:
            if (i % prime) == 0:
                primeX = False
                break
        if primeX:
            primes.append(i)
            yield i
test = genPrimes()

print(test.__next__())
print(test.__next__())
print(test.__next__())
print(test.__next__())
