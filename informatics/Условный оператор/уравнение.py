a = int(input())
b = int(input())
if b == 0 and a == 0:
    print("INF")
elif a == 0 and b != 0:
    print("NO")
elif a != 0 and b == 0:
    print(0)
else:
    x = -(b // a)
    if a * x + b == 0:
        print(x)
    elif a * x + b != 0:
        print("NO")

