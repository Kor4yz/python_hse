N = int(input())
s = 0
for i in range(0, N + 1):
    s += 2 ** i
print(s)