a = int(input())
b = int(input())
c = int(input())
if a == c == b:
    print(3)
elif (a == c and a != b and c != b) or (b == c and a != b and c != a) or (b == a and a != c and c != b):
    print(2)
else:
    print(0)