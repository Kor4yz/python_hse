n = int(input())
nuli = 0
pol = 0
otr = 0
for i in range(n):
    s = int(input())
    if s == 0:
        nuli += 1
    elif s > 0:
        pol += 1
    else:
        otr += 1
print(nuli, pol, otr)
