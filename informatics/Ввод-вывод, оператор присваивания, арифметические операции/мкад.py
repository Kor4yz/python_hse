v = int(input())
t = int(input())
s = 109
if v > 0:
    print((v*t) % s)
else:
    print((s + (v*t)) % s)

