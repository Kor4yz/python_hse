a = int(input())
b = int(input())
s = 0
for i in range(a, b + 1):
    s = i % 2
    if s == 0:
        print(i)
