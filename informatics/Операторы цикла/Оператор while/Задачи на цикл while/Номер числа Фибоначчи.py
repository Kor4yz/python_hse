A = int(input())
result = 1
f2 = 0
f0 = 0
f1 = 1
while f2 <= A:
    if f2 != A:
        f2 = f1 + f0
        f0 = f1
        f1 = f2
        result += 1
    elif f2 == A:
        break
if A == 1:
    print(f1)
elif A != f2:
    print(-1)
else:
    print(result)
