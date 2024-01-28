n = int(input())
nuli = 0
for i in range(n):
    s = int(input())
    if s == 0:
        nuli += 1
if nuli > 0:
    print("YES")
else:
    print('NO')

