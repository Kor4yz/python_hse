n = int(input())
nuli = 0
while n > 0:
    a = n % 10
    if a == 0:
        nuli += 1
    n = n // 10
print(nuli)
