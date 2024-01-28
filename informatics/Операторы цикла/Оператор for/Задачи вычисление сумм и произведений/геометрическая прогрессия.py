a = int(input())
n = int(input())
s = 0
for i in range(0, n + 1):
    s += a ** i
    print(s)
