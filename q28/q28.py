import math

arr = [3, 5, 7, 9]

def next_level(arr, level):
    se(arr, arr[0], level)
    sw(arr, arr[1], level)
    nw(arr, arr[2], level)
    ne(arr, arr[3], level)

def se(arr, start, level):
    increment = 2 * level
    arr[0] = start + 3 * increment + (2 * (level + 1))
def sw(arr, start, level):
    increment = 2 * level
    arr[1] = start + 2 * increment + 2 * (2 * (level + 1))
def nw(arr, start, level):
    increment = 2 * level
    arr[2] = start + 1 * increment + 3 * (2 * (level + 1))
def ne(arr, start, level):
    increment = 2 * level
    arr[3] = start + 4 * (2 * (level + 1))

total = 1
for i in range(1, 500 + 1):
    total += reduce(lambda x, y: x + y, arr) 
    next_level(arr, i)

print total

