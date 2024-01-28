import math
def F(num):
    n_digit = 0
    num2 = num
    while num2>0:
        n_digit = n_digit + 1
        num2 = num2//10
        t = num%10
        res = t*int(math.pow(10, n_digit -1))
    return res + F(num//10)
print(F(1234567))