fx = int(input())
fy = int(input())
dx = int(input())
dy = int(input())
if (fx == dx or fy == dy) or (abs(dx - fx) == abs(fy - dy)):
    print('YES')
else:
    print('NO')
    