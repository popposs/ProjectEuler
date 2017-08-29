def ascii_total(name):
    ord_arr = [(ord(c) - 64) for c in name[:-1]]
    return sum(ord_arr)

def check_triangle(m, n):
    return check_triangle_helper(m, n, 0)
    
def check_triangle_helper(m, n, i):
    if n > m[i]:
        while m[i] < n:
            i += 1
            m[i] = int(0.5 * i * (i + 1))
            if m[i] == n:
                return True
        return False
    else:
        return n in m

triangles = {}
triangles[0] = 0
triangles[1] = 1

file = open("final.txt", "r")
count = 0
for line in file:
    if check_triangle(triangles, ascii_total(line)):
        count += 1
    
print count
file.close()
