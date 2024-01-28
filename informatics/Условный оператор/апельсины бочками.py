from itertools import product

s = "01"
q = list(product(s, repeat = 15))

a = 0
b = 0

for i in q:
    q = "".join(i)
    b += 1
    if (q.count("0") == 5) and (q.count("1") == 10) and (q[0] == q[1] == q[2] == q[3] == q[4] == "1"):
        a += 1

print(a, b)
