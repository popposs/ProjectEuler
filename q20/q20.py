
factorial = [1, 1, 2]
for i in range(3, 100 + 1):
    factorial.append(i * factorial[i - 1])
print reduce(lambda x, y: x + y, map(int, str(factorial[100])))