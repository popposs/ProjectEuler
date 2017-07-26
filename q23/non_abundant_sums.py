import math
from operator import add
import timeit

# Returns list of proper divisors of n
def d(n):
    ret = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            ret += [i, n / i]

    return ret

def is_abundant(n):
    return sum(set(d(n))) > n

start = timeit.default_timer()
# Find the sum of all the positive integers which
# cannot be written as the sum of two abundant numbers.
# ---------------------------
abundants = {}
for i in range(1, 28123 + 1):
    if is_abundant(i):
        if not i in abundants:
            abundants[i] = 1

summable = {}
for b in range(24, 28123 + 1):
    for a in abundants:
        c = b - a
        if c < 12:
            break
        if c in abundants:
            summable[b] = 1
            break

total = 0
for i in range(0, 28123 + 1):
    if not i in summable:
        total += i 

# ---------------------------
stop = timeit.default_timer()
print 'Time:', stop - start 
print total