from copy import deepcopy

def next_permutation(arr):
    last = len(arr) - 1

    # find k
    k = -1
    for elem in range(last):
        if arr[elem] < arr[elem + 1]:
            if k < elem:
                k = elem

    if k == - 1:
        return -1

    # find l
    l = -1
    for elem in range(k + 1, len(arr)):
        if l < elem:
            if arr[k] < arr[elem]:
                l = elem
                            
    arr[k], arr[l] = arr[l], arr[k]

    first_half = arr[0 : k + 1]
    second_half = arr[k + 1 : last + 1]

    # reverse from k + 1 ==> n 
    if not len(second_half) == 1:
        second_half.reverse()

    return first_half + second_half

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

iteration = 1
ret = next_permutation(deepcopy(array))
while  ret != -1:
    iteration += 1
    ret = next_permutation(ret)
    if iteration == 1000000 - 1:
        print ret
        break
