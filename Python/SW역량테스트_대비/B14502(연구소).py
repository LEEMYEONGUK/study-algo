# 연구소
from collections import deque
from copy import deepcopy

def bfs(sr, sc, clst):
    q = deque((sr, sc))
    visited = [[0] * M for _ in range(N)]
    visited[sr][sc] = 1
    cnt = 0
    while q:
        r, c = q.popleft()
        cnt += 1
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and clst[nr][nc] == 0:
                q.append((nr, nc))
    return cnt

def dfs(n, tlst):
    if n == 3:
        if (2, 1) in tlst:
            print(tlst)
        return

    for r in range(N):
        for c in range(M):
            if 0 <= r < N and 0 <= c < M and lst[r][c] == 0:
                if dfs_visited[r][c] == 0:
                    dfs_visited[r][c] = 1
                    dfs(n + 1, tlst + [(r, c)])
                    dfs_visited[r][c] = 0




N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
print(lst)
dfs_visited = [[0] * M for _ in range(N)]
dfs(0, [])