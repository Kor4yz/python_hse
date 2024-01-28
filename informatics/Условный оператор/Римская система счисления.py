x = int(input())
a = 'I'
b = 'II'
c = 'III'
d = 'IV'
e = 'V'
f = 'VI'
g = 'VII'
q = 'VIII'
w = 'IX'
r = 'X'
t = 'XX'
y = 'XXX'
u = 'XL'
i = 'L'
o = 'LX'
p = 'LXX'
s = 'LXXX'
h = 'XC'
if x // 100 == 1:
    print("C")
else:
    if x // 10 == 9:
        if x % 10 == 9:
            print(h + w)
        elif x % 10 == 8:
            print(h + q)
        elif x % 10 == 7:
            print(h + g)
        elif x % 10 == 6:
            print(h + f)
        elif x % 10 == 5:
            print(h + e)
        elif x % 10 == 4:
            print(h + d)
        elif x % 10 == 3:
            print(h + c)
        elif x % 10 == 2:
            print(h + b)
        elif x % 10 == 1:
            print(h + a)
        elif x % 10 == 0:
            print(h)
    elif x // 10 == 8:
        if x % 10 == 9:
            print(s + w)
        elif x % 10 == 8:
            print(s + q)
        elif x % 10 == 7:
            print(s + g)
        elif x % 10 == 6:
            print(s + f)
        elif x % 10 == 5:
            print(s + e)
        elif x % 10 == 4:
            print(s + d)
        elif x % 10 == 3:
            print(s + c)
        elif x % 10 == 2:
            print(s + b)
        elif x % 10 == 1:
            print(s + a)
        elif x % 10 == 0:
            print(s)
    elif x // 10 == 7:
        if x % 10 == 9:
            print(p + w)
        elif x % 10 == 8:
            print(p + q)
        elif x % 10 == 7:
            print(p + g)
        elif x % 10 == 6:
            print(p + f)
        elif x % 10 == 5:
            print(p + e)
        elif x % 10 == 4:
            print(p + d)
        elif x % 10 == 3:
            print(p + c)
        elif x % 10 == 2:
            print(p + b)
        elif x % 10 == 1:
            print(p + a)
        elif x % 10 == 0:
            print(p)
    elif x // 10 == 6:
        if x % 10 == 9:
            print(o + w)
        elif x % 10 == 8:
            print(o + q)
        elif x % 10 == 7:
            print(o + g)
        elif x % 10 == 6:
            print(o + f)
        elif x % 10 == 5:
            print(o + e)
        elif x % 10 == 4:
            print(o + d)
        elif x % 10 == 3:
            print(o + c)
        elif x % 10 == 2:
            print(o + b)
        elif x % 10 == 1:
            print(o + a)
        elif x % 10 == 0:
            print(o)
    elif x // 10 == 5:
        if x % 10 == 9:
            print(i + w)
        elif x % 10 == 8:
            print(i + q)
        elif x % 10 == 7:
            print(i + g)
        elif x % 10 == 6:
            print(i + f)
        elif x % 10 == 5:
            print(i + e)
        elif x % 10 == 4:
            print(i + d)
        elif x % 10 == 3:
            print(i + c)
        elif x % 10 == 2:
            print(i + b)
        elif x % 10 == 1:
            print(i + a)
        elif x % 10 == 0:
            print(i)
    elif x // 10 == 4:
        if x % 10 == 9:
            print(u + w)
        elif x % 10 == 8:
            print(u + q)
        elif x % 10 == 7:
            print(u + g)
        elif x % 10 == 6:
            print(u + f)
        elif x % 10 == 5:
            print(u + e)
        elif x % 10 == 4:
            print(u + d)
        elif x % 10 == 3:
            print(u + c)
        elif x % 10 == 2:
            print(u + b)
        elif x % 10 == 1:
            print(u + a)
        elif x % 10 == 0:
            print(u)
    elif x // 10 == 3:
        if x % 10 == 9:
            print(y + w)
        elif x % 10 == 8:
            print(y + q)
        elif x % 10 == 7:
            print(y + g)
        elif x % 10 == 6:
            print(y + f)
        elif x % 10 == 5:
            print(y + e)
        elif x % 10 == 4:
            print(y + d)
        elif x % 10 == 3:
            print(y + c)
        elif x % 10 == 2:
            print(y + b)
        elif x % 10 == 1:
            print(y + a)
        elif x % 10 == 0:
            print(y)
    elif x // 10 == 2:
        if x % 10 == 9:
            print(t + w)
        elif x % 10 == 8:
            print(t + q)
        elif x % 10 == 7:
            print(t + g)
        elif x % 10 == 6:
            print(t + f)
        elif x % 10 == 5:
            print(t + e)
        elif x % 10 == 4:
            print(t + d)
        elif x % 10 == 3:
            print(t + c)
        elif x % 10 == 2:
            print(t + b)
        elif x % 10 == 1:
            print(t + a)
        elif x % 10 == 0:
            print(t)
    elif x // 10 == 1:
        if x % 10 == 9:
            print(r + w)
        elif x % 10 == 8:
            print(r + q)
        elif x % 10 == 7:
            print(r + g)
        elif x % 10 == 6:
            print(r + f)
        elif x % 10 == 5:
            print(r + e)
        elif x % 10 == 4:
            print(r + d)
        elif x % 10 == 3:
            print(r + c)
        elif x % 10 == 2:
            print(r + b)
        elif x % 10 == 1:
            print(r + a)
        elif x % 10 == 0:
            print(r)
    elif x // 10 == 0:
        if x % 10 == 9:
            print(w)
        elif x % 10 == 8:
            print(q)
        elif x % 10 == 7:
            print(g)
        elif x % 10 == 6:
            print(f)
        elif x % 10 == 5:
            print(e)
        elif x % 10 == 4:
            print(d)
        elif x % 10 == 3:
            print(c)
        elif x % 10 == 2:
            print(b)
        elif x % 10 == 1:
            print(a)
        elif x % 10 == 0:
            print("0")
