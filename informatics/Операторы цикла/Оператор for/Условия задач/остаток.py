a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = 1
for i in range(a, b + 1):
    s = i % d
    if s == c:
        print(i)