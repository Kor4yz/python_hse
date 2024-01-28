N = int(input())
i = 1
resultat = 0
while i <= N:
    if i == N:
        resultat = 1
    else:
        resultat = 0
    i = i * 2
if resultat == 1:
    print("YES")
else:
    print("NO")
