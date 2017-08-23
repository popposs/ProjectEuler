import math

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

def digit_length(n):
    count = 1
    while n / 10:
        n /= 10
        count += 1
    return count

max = 0
for i in range(100000, 0, -1):
    index = 1
    suffix = i * index
    curr = suffix
    index += 1
    while digit_length(curr) < 9:
        suffix = index * i
        curr = curr * 10 ** digit_length(suffix) + suffix
        index += 1

    if index > 1 and digit_length(curr) == 9 and unique(digits(curr)):
        if max < curr:
            max = curr

print max