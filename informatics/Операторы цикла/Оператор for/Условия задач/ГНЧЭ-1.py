n = int(input())
a = 1
b = 1
for i in range(1, n + 1):
    print(b)
    a += 1
    if a > b:
        b += 1
        a = 1
