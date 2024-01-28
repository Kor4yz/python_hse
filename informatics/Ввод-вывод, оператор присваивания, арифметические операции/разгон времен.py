h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
s4 = (s2 - s1) + ((m2 - m1) + (h2 - h1) * 60) * 60
print(s4)