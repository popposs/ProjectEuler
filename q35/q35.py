import math
import timeit

def prime_gen(n):
    sieve = [True] * n
    for m in xrange(3, int(math.sqrt(n)) + 1, 2):
        if sieve[m]:
            sieve[m * m :: 2 * m] = [False] * ((n - m * m - 1) / (2 * m) + 1)
    return [2] + [m for m in xrange(3, n, 2) if sieve[m]]

def digits(n):
    return map(int, str(n))

def circular_prime(arr, n):
    ret = []
    for i in range(n, n + len(arr)):
        ret.append(arr[i % len(arr)])

    int_num = int(reduce(lambda x, y: x + y, map(str, ret)))
    return int_num

start = timeit.default_timer()

circular_primes = {}
primes = {}
for i in prime_gen(1000000):
    primes[i] = 1

for i in primes:
    d = digits(i)
    curr_primes = []
    prime = True
    for x in range(len(d)):
        curr = circular_prime(d, x)
        if curr in primes:
            curr_primes.append(curr)
        else:
            prime = False
            break
    if prime:
        for elem in curr_primes:
            circular_primes[elem] = 1

stop = timeit.default_timer()
print 'Time:', stop - start 
print 'Number of Primes:', len(circular_primes.keys()) 
