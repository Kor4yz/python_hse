limit = 100000
a, b, n = int(input()), int(input()), int(input())
mn, mx = 'A', 'B'
real = False
if a > b:
    mn, mx = 'B', 'A'
    a += b
    b = a - b
    a -= b
av, bv, k = 0, 0, 0
while k <= limit:
    k += 2
    if b - bv >= a:
        bv += a
    else:
        bv = a - (b - bv)
        k += 2
    if n == bv:
        real = True
        break
if real:
    bv = 0
    while True:
        print(f'>{mn}\n{mn}>{mx}')
        if b - bv >= a:
            bv += a
        else:
            bv = a - (b - bv)
            print(f'{mx}>\n{mn}>{mx}')
            if n == bv:
                break
else:
    print('Impossible')