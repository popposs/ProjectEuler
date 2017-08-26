def digits(n):
    return map(int, str(n))

length = 0
i = 1
ret = []
curr_target = 1
while length <= 1000000:
    d = digits(i)
    if length + len(d) > curr_target * 10:
        ret.append(d[curr_target * 10 - length - 1])
        curr_target *= 10
    length += len(d)
    if length == curr_target:
        ret.append(i)

    i += 1

print ret, reduce(lambda x,y: x * y, ret)