def dfs(n, s):
    if s == N:
        print(n)
        return
    for j in range(1, lst[s]):
        dfs(n + 1, s + j)

N = int(input())

lst = list(map(int, input().split()))

dfs(0, 0)