import math
import timeit

# Returns list of proper divisors of n
def d(n):
    ret = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            ret += [i, n / i]

    return sum(ret)

# Return sum of amicable pair
def amicable(a):
    b = d(a)
    if a != b and d(b) == a:
        return [a, b]
    else:
        return [0]

start = timeit.default_timer()
# Maps to prevent double counting
total = {}
other_pair = {}

for i in range(1, 10000):
    if i not in other_pair: 
        pair = amicable(i)
        total[i] = sum(pair) 

        if len(pair) == 2:
            other_pair[pair[1]] = 1

stop = timeit.default_timer()
print sum(total.values())
print 'Time:', stop - start 
