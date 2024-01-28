N = int(input())
s = 1
e = 0
for i in range(1, N + 1):
    s = s * i
    e += 1/s
print(e + 1)
