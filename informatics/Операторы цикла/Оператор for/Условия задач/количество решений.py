a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = 0
for x in range(0, 1001):
    if (x - e) != 0:
        if ((a * (x ** 3) + b * (x ** 2) + c * x + d) / (x - e)) == 0:
            f += 1
print(f)

