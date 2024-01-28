a = int(input())
b = int(input())
c = int(input())
d = 0
if a <= b <= c:
    print(a, b, c)
elif a <= c <= b:
    d = b
    b = c
    c = d
    print(a, b, c)
elif b <= a <= c:
    d = a
    a = b
    b = d
    print(a, b, c)
elif c <= a <= b:
    d = b
    b = a
    a = c
    c = d
    print(a, b, c)
elif c <= b <= a:
    d = a
    a = c
    c = d
    print(a, b, c)
else:
    d = a
    a = b
    b = c
    c = d
    print(a, b, c)
