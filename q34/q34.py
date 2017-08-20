factorial_arr = {}
factorial_arr[0] = 1
factorial_arr[1] = 1
factorial_arr[2] = 2
for i in range(3, 10):
    factorial_arr[i] = i * factorial_arr[i - 1]

def factorial(n):
    if not n in factorial_arr:
        factorial_arr[n] = n * factorial_arr[n - 1]
    return factorial_arr[n]

def digits(n):
    m = map(int, str(n))
    total = 0
    for i in m:
        total += factorial(i)
    return total

sum = 0
for i in xrange(3, 99999):
    if digits(i) == i:
        sum += i
print sum
