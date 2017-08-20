def digits(a, b):
    digits_a = map(int, str(a))
    digits_b = map(int, str(b))

    a_map = {}
    a_map[0] = digits_a[1]
    a_map[1] = digits_a[0]

    b_map = {}
    b_map[0] = digits_b[1]
    b_map[1] = digits_b[0]
    for i in range(2):
        for j in range(2):
            if a_map[i] == b_map[j] and b_map[i] != 0:
                if b != 0 and 1.0 * a_map[j] / b_map[i] == 1.0 * a / b:
                    return a_map[j], b_map[i]
                
total = 1
for i in range(10, 100):
    for j in range(10, 100):
        ret = digits(i, j)
        if ret != None:
            a, b = ret
            if a / b < 1:
                total *= 1. * a / b

print total
