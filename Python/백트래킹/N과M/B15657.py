# N과 M(8)
def dfs(n, s, tlst):
    if n == M:
        print(*tlst)
        return
    for j in range(s, N):
        dfs(n + 1, j, tlst + [lst[j]])

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
dfs(0, 0, [])