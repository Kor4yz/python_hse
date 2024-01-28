a = 0 # по 1 п
b = 0 # по 10 п
c = 0 # по 60 п
n = int(input())
if n % 60 > 34:
    c = n // 60 + 1
    print(a, b, c)
else:
    if n % 10 > 8:
        c = n // 60
        b = n % 60 // 10 + 1
        print(a, b, c)
    else:
        c = n // 60
        b = n % 60 // 10
        a = n % 60 % 10
        print(a, b, c)
