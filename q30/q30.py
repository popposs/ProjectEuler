def digits(n):
    return map(int, str(n))

def fifth_power(arr):
    return reduce(lambda x, y: x + y, map(lambda x: x ** 5, arr))

total = 0
val = 2
while val < 999999:
    curr = fifth_power(digits(val))
    if curr == val:
        total += curr
    val += 1

print total