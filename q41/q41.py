from math import sqrt
from itertools import count, islice
from copy import deepcopy

def isPrime(n):
    if n < 2: return False
    for number in islice(count(2), int(sqrt(n) - 1)):
        if not n % number:
            return False
    return True

def next_permutation(arr):
    last = len(arr) - 1

    # find k
    k = -1
    for elem in range(last - 1, -1, -1):
        if arr[elem] > arr[elem + 1]:
            if k < elem:
                k = elem

    if k == - 1:
        return -1

    # find l
    l = -1
    curr = k
    for elem in range(k + 1, len(arr)):
        if l < elem:
            if arr[k] > arr[elem]:
                l = elem

    arr[k], arr[l] = arr[l], arr[k]

    first_half = arr[0 : k + 1]
    second_half = arr[k + 1 : last + 1]

    # reverse from k + 1 ==> n 
    if not len(second_half) == 1:
        second_half = sorted(second_half, reverse = True)

    return first_half + second_half

def isPandigital(arr):
    m = {}
    max = 0
    for elem in arr:
        if not elem in m:
            if max < elem:
                max = elem
            m[elem] = 1
    
    for i in range(1, max + 1):
        if not i in m:
            return False
    return True

arr = [7, 6, 5, 4, 3, 2, 1]
ret = next_permutation(deepcopy(arr))
while  ret != -1:
    ret = next_permutation(ret)
    if ret == -1:
        break
    num = int(reduce(lambda x,y: x + y, map(str, ret)))
    if isPandigital(ret) and isPrime(num):
        print num 
        break
