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
abundants = []
for i in range(1, 28123 + 1):
    if is_abundant(i):
        abundants.append(i)

abundant_sums = []
for i in range(len(abundants)):
    curr_list = []
    for j in range(len(abundants)):
        curr_list.append(abundants[(i + j) % len(abundants)])
    added = map(add, curr_list, abundants) 
    abundant_sums.append(added)

sums = [item for sublist in abundant_sums for item in sublist]
# ---------------------------
stop = timeit.default_timer()
print 'Time:', stop - start 
sums = set(sums)
print sums