from collections import defaultdict
import timeit

target = 200 + 1
coin_set = [1, 2, 5, 10, 20, 50, 100, 200]
ways = defaultdict(lambda: 0, {})
ways[1] = 1

start = timeit.default_timer()
for coin in coin_set:
    for i in range(coin, target + 1):
        ways[i] += ways[i - coin]

stop = timeit.default_timer()
print 'Time:', stop - start 
print ways[target]