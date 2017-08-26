import math
import timeit

def pythagorean_triples(limit):
    c = 0
    m = 2
    while(c < limit):
        for n in range(1, m + 1):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            if(c > limit):
                break
            if(a == 0 or b == 0 or c == 0):
                break
            yield [a, b, c]
        m = m + 1

start = timeit.default_timer()
ways = {}
for triangle in pythagorean_triples(1000):
    p = reduce(lambda x, y: x + y, triangle)
    temp_tri = triangle
    temp_p = p
    index = 2
    while temp_p <= 1000:
        if temp_tri[0] ** 2 + temp_tri[1] ** 2 == temp_tri[2] ** 2:
            if not temp_p in ways:
                ways[temp_p] = [set(temp_tri)]
            else:
                if not set(temp_tri) in ways[temp_p]:
                    ways[temp_p] += [set(temp_tri)]
        temp_tri = [x * index for x in triangle]
        index += 1
        temp_p = temp_tri[0] + temp_tri[1] + temp_tri[2]

max_p = 0
max_p_val = 0

for key, value in ways.iteritems():
    if len(value) > max_p_val:
        max_p_val = len(value)
        max_p = key

stop = timeit.default_timer()
print 'Time:', stop - start 

print max_p, max_p_val
