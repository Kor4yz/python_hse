x = int(input())
for i in range(2, 30001):
    if x % i == 0:
        s = i
        break
print(s)

