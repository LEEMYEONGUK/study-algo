# 거스름돈
#
# n = int(input())
#
# sm = 0
# cnt = 0
# while True:
#     sm += 5
#     cnt += 1
#     if sm == n:
#         # print(cnt)
#         break
#     if sm > n:
#         sm -= 5
#         cnt -= 1
#         if (n - sm) % 2 == 0:
#             cnt += (n - sm)//2
#             break
#         else:
#             sm -= 5
#             cnt -= 1
#             if (n - sm) % 2 == 0:
#                 cnt += (n - sm)//2
#                 break
#             else:
#                 cnt = -1
#                 break
#
# print(cnt)

n = int(input())
cnt = 0

if n % 5 == 0:
    print(n//5)
else:
    while True:
        n -= 2
        cnt += 1
        if n % 5 == 0:
            cnt += n // 5
            break
        if n < 0:
            cnt = -1
            break

    print(cnt)
