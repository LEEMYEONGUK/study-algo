# 연구소 2
from collections import deque

# 입력 5번 부터
# 바이러스 못 퍼트릴때 -1 출력 구현하기


def bfs(b_lst):
    b_visited = [[0] * N for _ in range(N)]
    b_lst = deque(b_lst)
    for i, j in b_lst:
        b_visited[i][j] = 1

    while b_lst:
        r, c = b_lst.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and lst[nr][nc] == 0 and b_visited[nr][nc] == 0:
                b_lst.append((nr, nc))
                b_visited[nr][nc] = b_visited[r][c] + 1

    max_v = 0
    b_cnt = 0
    for a in range(N):
        for b in range(N):
            max_v = max(max_v, b_visited[a][b])

    return max_v


def dfs(n, tlst):
    global min_result
    if n == M:
        # print(tlst)
        min_result = min(min_result, bfs(tlst))
        return
    for j in range(V):
        if visited[j] == 0:
            visited[j] = 1
            dfs(n + 1, tlst+[v_lst[j]])
            visited[j] = 0


N, M = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(N)]

print(lst)
# 바이러스 위치 찾기
v_lst = []
# 0의 개수
cnt = 0
for r in range(N):
    for c in range(N):
        if lst[r][c] == 2:
            v_lst.append((r, c))
        if lst[r][c] == 0:
            cnt += 1

V = len(v_lst)
visited = [0] * V
min_result = 100000
dfs(0, [])
print(v_lst)
print(min_result)