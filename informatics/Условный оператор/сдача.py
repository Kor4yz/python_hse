a = int(input()) # руб товар
b = int(input()) # копеек товар
c = int(input()) # руб заплатит
d = int(input()) # копеек заплатит
if a > c or (a * 100 + b == c * 100 + d):
    print(0, 0)
else:
    g = (c * 100 + d) - (a * 100 + b)
    f = g % 100
    e = g // 100
    print(e, f)
