def ascii_total(name):
    ord_arr = [(ord(c) - 64) for c in name]
    print name, ord_arr
    return sum(ord_arr)
def total_score(pos, ascii_val):
    return int(pos) * ascii_val

file = open("final.txt", "r")
total = 0
for line in file:
    arr = line.split()
    total = total_score(arr[0], ascii_total(arr[1]))

file.close()
print 'TOTAL:', total
