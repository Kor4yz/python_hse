max = 0
sum = 0
maxsum = 0
a = int(input())
while a != 0:
    if max == a:
        sum += 1
    else:
        max = a
        if maxsum <= sum:
            maxsum = sum
        sum = 1
    a = int(input())
if maxsum > sum:
    maxsum = maxsum
else:
    maxsum = sum
print(maxsum)
