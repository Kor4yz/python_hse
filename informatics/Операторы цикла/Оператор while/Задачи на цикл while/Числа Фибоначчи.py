n = int(input())
result = 1
f2 = 0
f0 = 0
f1 = 1
while result < n:
    f2 = f1 + f0
    f0 = f1
    f1 = f2
    result += 1
if n == 1:
    print(f1)
else:
    print(f2)