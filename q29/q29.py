distinct = {}
size = 0
for a in range(2, 101):
    for b in range(2, 101):
        value = a ** b
        if value in distinct:
            continue
        distinct[value] = 1
        size += 1

print size
