x = int(input())
y = int(input())
resultat = 1
while x < y:
    x = x + x * 0.1
    resultat += 1
print(resultat)
