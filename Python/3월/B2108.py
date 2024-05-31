import sys
input = sys.stdin.readline
N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
arr_sum = sum(arr)

# 평균
# if arr_sum >= 0:
#     if 0 <= arr_sum/N - int(arr_sum/N) < 0.5:
#         print(arr_sum//N)
#     elif 0.5 <= arr_sum/N - int(arr_sum/N) < 1:
#         print(arr_sum//N + 1)
# elif arr_sum < 0:
#     if 0 <= abs(arr_sum/N - int(arr_sum/N)) < 0.5:
#         print(arr_sum//N + 1)
#     elif 0.5 <= abs(arr_sum/N - int(arr_sum/N)) < 1:
#         print(arr_sum//N)
print(round(arr_sum/N))

# 중앙값
print(arr[(N - 1)//2])

# 최빈값
mode_dic = dict()
for i in arr:
    if i in mode_dic:
        mode_dic[i] += 1
    else:
        mode_dic[i] = 1
# print(mode_dic)

mode = max(mode_dic.values())
mode_lst = []

for k in mode_dic:
    if mode_dic[k] == mode:
        mode_lst.append(k)

if len(mode_lst) == 1:
    print(*mode_lst)
else:
    print(mode_lst[1])

# mode = 0
# mode_num = 0
# mode_arr = []
#
# for i in arr:
#     if mode < arr.count(i):
#         mode = arr.count(i)
#         mode_num = i
#
# mode_arr.append(mode_num)
#
# for i in arr:
#     if mode == arr.count(i):
#         if i not in mode_arr:
#             mode_arr.append(i)
# mode_arr.sort()
#
# if len(mode_arr) == 1:
#     print(mode_num)
# else:
#     print(mode_arr[1])

# 범위
print(arr[-1]-arr[0])
