import math
import timeit
from functools import reduce

def digits(n):
    return map(int, str(n))

def flatten(l):
    return [elem for sublist in l for elem in sublist]

def unique(arr):
    flat = []
    for i in arr:
        d = digits(i)
        flat.append(d)
    flat = flatten(flat)

    m = {}
    if len(flat) == 9:
        for digit in flat:
            if digit in m:
                return False
            m[digit] = 1

    for i in range(1, 10):
        if not i in m:
            return False
    return True

def divisors(n):
    ret = [1, n]
    for i in xrange(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            ret += [i, n / i]
    return ret

def pandigital(n):
    arr = divisors(n)
    for i in xrange(0, len(arr), 2): 
        val = arr[i : i + 2] + [n]
        if unique(val):
            return True
    return False

start = timeit.default_timer()
pandigitals = filter(lambda x: pandigital(x), xrange(9999))
total = reduce(lambda x, y: x + y, pandigitals)

stop = timeit.default_timer()
print 'Time:', stop - start
print pandigitals 
print 'Total:', total 
