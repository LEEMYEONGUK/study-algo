# 좌표압축
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
s_lst = sorted(set(lst))
dic = dict()
answer = [0] * N
for i in range(len(s_lst)):
    dic[s_lst[i]] = i
for i in range(N):
    answer[i] = dic[lst[i]]
print(*answer)



# s_lst = set(lst)
# c_lst = list(s_lst)
# n_lst = [0] * N
# for i in range(N):
#     cnt = 0
#     for j in range(len(c_lst)):
#         if lst[i] > c_lst[j]:
#             cnt += 1
#     n_lst[i] = cnt
#
# print(*n_lst)