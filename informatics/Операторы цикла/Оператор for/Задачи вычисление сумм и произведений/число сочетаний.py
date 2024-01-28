n = int(input())
k = int(input())
s = 1
for i in range(1, n + 1):
    s = s * i
q = 1
for i in range(1, k + 1):
    q = q * i
e = 1
for i in range(1, (n - k) + 1):
    e = e * i
itog = s/(q*e)
print(int(itog))
