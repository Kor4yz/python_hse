n = int(input())
h = (n // (60**2)) % 24
m = ((n // 60) % 60)
s = (n % 60)
if m < 10 and s < 10:
    print(h, ":", "0", m, ":", "0", s, sep="")
elif m < 10:
    print(h, ":", "0", m, ":",  s, sep="")
elif s < 10:
    print(h, ":",  m, ":", "0", s, sep="")
elif s > 10 and m > 10:
    print(h, ":", m, ":", s, sep="")
# семь попыток ахуеть я даун