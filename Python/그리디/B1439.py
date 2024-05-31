# 뒤집기

lst = list(input())
if lst[-1] == 1:
    lst += [0]
else:
    lst += [1]

cnt = 0
for i in range(len(lst) - 1):
    if lst[i] != lst[i+1]:
        cnt += 1
print(cnt//2)