N = int(input())
i = 1
while i <= N:
    if i % i ** 0.5 == 0:
        print(i)
    i += 1

