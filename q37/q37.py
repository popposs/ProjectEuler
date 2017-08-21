import math
import timeit

def prime_gen(n):
    sieve = [True] * n
    for m in xrange(3, int(math.sqrt(n)) + 1, 2):
        if sieve[m]:
            sieve[m * m :: 2 * m] = [False] * ((n - m * m - 1) / (2 * m) + 1)
    return [2] + [m for m in xrange(3, n, 2) if sieve[m]]

def truncatable(n):
    length = 1
    x = n
    while x / 10:
        x /= 10
        length += 1
    x = n
    for i in xrange(1, length + 1):
        if not x in primes:
            return False
        x /= 10 

    x = n
    for i in xrange(1, length + 1):
        if not n in primes:
            return False
        n = n % 10 ** (length - i)
    return True

start = timeit.default_timer()

primes = {}
for i in prime_gen(1000000):
    primes[i] = 1

sum = 0
num = 0
i = 0

for i in primes:
    if i < 11:
        continue
    if num >= 11:
        break
    if truncatable(i):
        print i
        sum += i
        num += 1
    i += 1

stop = timeit.default_timer()
print 'Time:', stop - start 
print sum
