lastmax = int(input())
max = int(input())
if lastmax > max:
    max, lastmax = lastmax, max
while(True):
    a = int(input())
    if a == 0:
        break
    if a > max:
        lastmax = max
        max = a
    elif a > lastmax:
        lastmax = a
print(lastmax)
