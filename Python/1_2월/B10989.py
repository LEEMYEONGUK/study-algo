# N = int(input())
#
# num_list = []
#
# for _ in range(N):
#     num_list.append(int(input()))
#
# for i in range(N-1, 0, -1):
#     for j in range(i):
#         if num_list[j] > num_list[j + 1]:
#             num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
#
# print(*num_list, sep="\n")

import sys
input = sys.stdin.readline

N = int(input())

lst = [0]*10001

for _ in range(N):
    lst[int(input())] += 1

for i in range(10001):
    if lst[i] > 0:
        for _ in range(lst[i]):
            print(i)

