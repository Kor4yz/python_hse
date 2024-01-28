sx = int(input())
sy = int(input())
dx = int(input())
dy = int(input())
if (sx != dx and sy != dy) and (abs(dx - sx) == abs(sy - dy)):
    print('YES')
else:
    print('NO')
