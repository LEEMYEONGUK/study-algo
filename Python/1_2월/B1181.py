N = int(input())

lst = []

for _ in range(N):
    lst.append(input())

lst = set(lst)
lst = list(lst)

lst.sort()
lst.sort(key=len)

print(*lst, sep="\n")

# for i in range(len(lst) - 1, 0, -1):
#     for j in range(i):
#         if len(lst[j]) > len(lst[j + 1]):
#             lst[j], lst[j + 1] = lst[j + 1], lst[j]

# for i in range(len(lst) - 1, 0, -1):
#     for j in range(i):
#         if len(lst[j]) == len(lst[j + 1]):
#             for k in range(len(lst[j])):
#                 if ord(lst[j][k]) == ord(lst[j + 1][k]):
#                     pass
#
#                 if ord(lst[j][k]) > ord(lst[j + 1][k]):
#                     lst[j], lst[j + 1] = lst[j + 1], lst[j]
#                     break
