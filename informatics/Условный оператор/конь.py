fx = int(input())
fy = int(input())
dx = int(input())
dy = int(input())
if (abs(fx - dx) == 1 and abs(fy - dy) == 2) or (abs(fx - dx) == 2 and abs(fy - dy) == 1):
    print('YES')
else:
    print('NO')
