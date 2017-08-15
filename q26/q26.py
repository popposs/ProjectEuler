def divide(n):
    return 1. / n

def repeat(n):
    q = n # denominator 
    k = 1 # period length, smallest k that q divides (10^k - 1)
    while (10 ** k - 1) % q != 0:
        k += 1
    return k

max = 0
index = 0
for i in range(2, 1000):
    if i % 2 != 0 and i % 5 != 0:
        r = repeat(i)
        if max < r:
            max = r
            index = i

print index

