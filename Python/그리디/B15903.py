# 카드 합체 놀이

n, m = map(int, input().split())

lst = list(map(int, input().split()))

for _ in range(m):
    lst.sort()
    sm = lst[0] + lst[1]
    lst[0] = sm
    lst[1] = sm

print(sum(lst))