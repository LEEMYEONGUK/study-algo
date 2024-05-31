# N과 M (12)

# n 고른 횟수, n = 0 이면 고른거 없다는 것
# 숫자, 비내림차순, 중복 사용 가능한지, visited 배열, start 위치, prev 사용?
def dfs(n, s, tlst):
    if n == M:
        print(*tlst)
        return
    prev = 0
    for j in range(s, N):
        if prev != lst[j]:
            prev = lst[j]
            dfs(n + 1, j, tlst + [lst[j]])

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
dfs(0, 0, [])
