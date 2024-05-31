# n-queen
# 같은 행 과 열, 대각선에 있으면 안됨

def dfs(sr, sc):
    visited[sr][sc] = 1


N = int(input())

for r in range(N):
    for c in range(N):
        visited = [[0] * N for _ in range(N)]
        dfs(r, c)