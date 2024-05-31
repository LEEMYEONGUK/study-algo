N, M = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()
sum_lst = []


for i in range(N):
    for j in range(N):
        if i != j:
            for k in range(N):
                if k != i and k != j:
                    if lst[i] + lst[j] + lst[k] <= M:
                        sum_lst.append(lst[i] + lst[j] + lst[k])

print(max(sum_lst))
