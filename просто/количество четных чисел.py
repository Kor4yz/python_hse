# дано число n затем n чисел найти количество четных чисел
n = int(input())
k = 0 #счетчик
for i in range(n):
    x = int(input())
    if (x % 2 == 0 ):
        k = k + 1
print(k)