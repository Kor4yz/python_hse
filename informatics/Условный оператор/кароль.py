fx = int(input())
fy = int(input())
dx = int(input())
dy = int(input())
D1 = abs(fx - dx)
D2 = abs(fy - dy)
if D1 + D2 == 1 or D1 * D2 == 1: # if fx + 1 == dx or fx - 1 == dx or fy + 1 == dy or fy - 1 == dy or abs(dx - fx) == 1 or abs(fy - dy) == 1
    print('YES')
else:
    print('NO')
