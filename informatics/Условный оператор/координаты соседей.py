M, N = map(int, input() .split())
x, y = map(int, input() .split())
if N > 1:
    if y == 1:
        print(x, y + 1)
    elif y == N:
        print(x, y - 1)
    else:
        print(x, y - 1)
        print(x, y + 1)
if M > 1:
    if x == 1:
        print(x + 1, y)
    elif x == M:
        print(x - 1, y)
    else:
        print(x - 1, y)
        print(x + 1, y)
# if M == x and N == y and x > 1 and y > 1:
#     print(M - 1, N)
#     print(M, N - 1)
# else:
#     if M == x and x > 1 and y == 1:
#         print(M - 1, N)
#         print(M, N + 1)
#     else:
#         if N == y and x == 1 and y > 1:
#             print(M + 1, N)
#             print(M, N - 1)
#         else:
#             if x == 1 and y == 1:
#                 print(x + 1, y)
#                 print(x, y + 1)
#             else:
#                 if x == 1 and N != y and y != 1:
#                     print(x, y + 1)
#                     print(x, y - 1)
#                     print(x + 1, y)
#                 else:
#                     if N == y and x != 1 and x != M:
#                         print(x + 1, y)
#                         print(x, y - 1)
#                         print(x - 1, y)
#                     else:
#                         if M == x and y != N and y > 1:
#                             print(x, y + 1)
#                             print(x, y - 1)
#                             print(x - 1, y)
#                         else:
#                             if y == 1 and x != 1 and x != M:
#                                 print(x, y + 1)
#                                 print(x - 1, y)
#                                 print(x + 1, y)
#                             else:
#                                 print(x, y + 1)
#                                 print(x + 1, y)
#                                 print(x, y - 1)
#                                 print(x - 1, y)
