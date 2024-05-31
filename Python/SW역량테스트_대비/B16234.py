# 인구 이동
import copy
from collections import deque
import copy
import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
def bfs(sr, sc):
    answer = {}
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = k
    cnt = 1
    sm = lst[sr][sc]
    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and L <= abs(lst[r][c]-lst[nr][nc]) <= R:
                cnt += 1
                sm += lst[nr][nc]
                visited[nr][nc] = k
                q.append((nr, nc))

        mn = sm // cnt
        answer[k] = mn

    for i in range(N):
        for j in range(N):
            if visited[i][j] == k:
                lst[i][j] = answer[k]

N, L, R = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

k = 1
answer_cnt = 0
while True:
    compare_lst = copy.deepcopy(lst)
    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if visited[r][c] == 0:
                bfs(r, c)
                k += 1
    if compare_lst == lst:
        break
    answer_cnt += 1

# print(visited)
# print(lst)
print(answer_cnt)