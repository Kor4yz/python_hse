n = int(input())
min = 0
max = 0
while n > 0:
    a = n % 10
    if a > min:
        min = a
    if min > max:
        max, min = min, max
    n = n // 10
print(min, max)
