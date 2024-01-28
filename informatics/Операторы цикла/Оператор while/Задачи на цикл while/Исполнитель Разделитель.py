A = int(input())
B = int(input())
while A != B:
    if (A - (A // 2)) >= B and A % 2 == 0:
        A = A // 2
        print(':2')
    elif (A - 1) > B or A % 2 == 1:
        A = A - 1
        print('-1')
