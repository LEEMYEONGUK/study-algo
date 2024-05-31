import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())

visited = [0] * (10 ** 6)
def dfs(s, i):
    visited[s] = i
    for d in [s + 1, s * 2, s * 3]:
        visited[d] = visited[s] + 1
        if d == N:
            return
        dfs(d, i + 1)


dfs(1, 1)
print(visited[N] - 1)