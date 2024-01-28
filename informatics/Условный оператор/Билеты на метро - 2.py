a = 0 # по 1 п
b = 0 # по 5 п
c = 0 # по 10 п
d = 0 # по 20 п
e = 0 # по 60 п
n = int(input())
if n % 60 > 35:
    e = n // 60 + 1
    print(a, b, c, d, e)
else:
    if n % 20 > 17:
        e = n // 60
        d = n % 60 // 20 + 1
        print(a, b, c, d, e)
    else:
        if n % 10 > 8:
            e = n // 60
            d = n % 60 // 20
            c = n % 60 % 20 // 10 + 1
            print(a, b, c, d, e)
        else:
            if n % 5 > 4:
                e = n // 60
                d = n % 60 // 20
                c = n % 60 % 20 // 10
                b = n % 60 % 20 % 10 // 5 + 1
                print(a, b, c, d, e)
            else:
                e = n // 60
                d = n % 60 // 20
                c = n % 60 % 20 // 10
                b = n % 60 % 20 % 10 // 5
                a = n % 60 % 20 % 10 % 5
                print(a, b, c, d, e)
