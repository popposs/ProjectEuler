from operator import add
array = [1,2,3]
for i in range(len(array)):
    curr = []
    for j in range(len(array)):
        curr.append(array[(i + j) % len(array)])
    print curr, '+', array, '=', map(add, curr, array)

