k = int(input())
n = (k / 4 - 1)**2
if k == 0:
    print('NO')
elif k == 1:
    print('YES')
elif ( (int) (n+k) ** 0.5) ** 2 == n + k:
    print('YES')
else:
    print('NO')
