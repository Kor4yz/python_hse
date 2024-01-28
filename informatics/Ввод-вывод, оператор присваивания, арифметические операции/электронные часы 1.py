n = int(input())
k = 0
if n >= 1440:
    k = (n % 1440) // 60
    b = n % 60
    print(k, b)
else:
    k = n // 60
    b = n % 60
    print(k, b)
    