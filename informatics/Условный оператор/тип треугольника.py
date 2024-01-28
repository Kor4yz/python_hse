a = float(input())
b = float(input())
c = float(input())
if a + b > c and a + c > b and b + c > a:
    if c > a and c > b:
        if c == (b ** 2 + a ** 2) ** 0.5:
            print("right")
        elif c > (b ** 2 + a ** 2) ** 0.5:
            print("obtuse")
        else:
            print("acute")
    elif a > c and a > b:
        if a == (b ** 2 + c ** 2) ** 0.5:
            print("right")
        elif a > (b ** 2 + c ** 2) ** 0.5:
            print("obtuse")
        else:
            print("acute")
    elif b > c and b > a:
        if b == (a ** 2 + c ** 2) ** 0.5:
            print("right")
        elif b > (a ** 2 + c ** 2) ** 0.5:
            print("obtuse")
        else:
            print("acute")
    else:
        print("acute")
else:
    print("impossible")
