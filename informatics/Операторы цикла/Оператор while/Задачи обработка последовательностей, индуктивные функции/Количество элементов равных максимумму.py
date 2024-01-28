max = int(input())
sum = 1
while(True):
    a = int(input())
    if a == 0:
        break
    if a == max:
        sum += 1
    elif a > max:
        max = a
        sum = 1
print(sum)
