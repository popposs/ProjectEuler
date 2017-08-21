import timeit

def to_binary(n):
    return "{0:b}".format(n)

def digits(n):
    return map(int, str(n))

def is_palindromic(n):
    d = digits(n)
    length = len(d)
    end = int(length / 2) + (length % 2 == 0)
    for i in xrange(end):
        if d[i] != d[length - i - 1]:
            return False

    d = digits(to_binary(n))
    length = len(d)
    end = int(length / 2) + (length % 2 == 0)
    for i in xrange(end):
        if d[i] != d[length - i - 1]:
            return False
    
    return True
        
start = timeit.default_timer()
total = 0
for i in xrange(1000000):
    if is_palindromic(i):
        total += i
print total
stop = timeit.default_timer()
print 'Time:', stop - start 

