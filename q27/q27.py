import math

class Quadratic:
    a = 0
    b = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "<a:%s b:%s>" % (self.a, self.b)

def isPrime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def quadratic_equation(n, a, b):
    return n ** 2 + a * n + b

primes = {}
for i in range(2, 1000 + 1):
    if isPrime(i):
        if i > 1000:
            break
        primes[i] = 1

max_quadratic = Quadratic(0, 0)
max_length = 0
for b in primes:
    for a in range(-999, 1000):
        n = 0
        length = 0
        while quadratic_equation(n, a, b) in primes:
            length += 1
            n += 1

        if max_length < length:
            max_length = length
            max_quadratic = Quadratic(a, b)

# print max_quadratic, max_length
print max_quadratic.a * max_quadratic.b
