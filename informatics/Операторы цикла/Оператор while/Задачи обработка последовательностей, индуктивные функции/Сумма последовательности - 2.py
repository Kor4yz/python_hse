sum = 0
sum0 = 0
while(True):
    a = int(input())
    if a == 0:
        sum0 += 1
        if sum0 == 2:
            break
    elif a != 0:
        sum += a
        sum0 = 0
print(sum)
