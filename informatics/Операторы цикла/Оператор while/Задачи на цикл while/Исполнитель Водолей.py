limit = 10 ** 4
k = 0
resultat = 0
A = int(input()) # литров в А сосуде
B = int(input()) #  литров в В сосуде
N = int(input()) # Сколько литров нужно получить
if A == B:
    if N != A:
        print("Impossible")
while k <= limit:
    k += 1
    if (A - (B * k)) >= 0:
        resultat = A - (B * k)
        if resultat == N:
            print(">A")
            print('B>')
            print('A>B')
        else:
            resultat = (((A // B) + 1) * 3) - 5
            if resultat == N:
                print(">A")
                print('A>B')
                print("B>")
                print('A>B')
            else:
                print("Impossible")
    else:
        A, B = B, A
        if (A - (B * k)) >= 0:
            resultat = A - (B * k)
            if resultat == N:
                print(">A")
                print('B>')
                print('A>B')
            else: 
                resultat = (((A // B) + 1) * 3) - 5
                if resultat == N:
                    print(">A")
                    print('A>B')
                    print(">A")
                    print('A>B')
                else:
                    print("Impossible")
                    print(2+3)