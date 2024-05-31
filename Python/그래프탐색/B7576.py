# 토마토
# BFS
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    while que:
        r, c = que.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and adjm[nr][nc] == 0:
                que.append((nr, nc))
                # 기준의 주변 토마토가 하루 후에 익기 때문에 1 더해주기
                adjm[nr][nc] = adjm[r][c] + 1

def find():
    max_v = -1
    # 배열을 순회하며
    for r in range(N):
        for c in range(M):
            # 익지 않은 토마토가 있을 시 -1 반환
            if adjm[r][c] == 0:
                return -1
            # 할당 된 값을 비교하며 최댓값 찾기
            if max_v < adjm[r][c]:
                max_v = adjm[r][c]
    # 시작을 1로 했으니 1 빼주기
    # (처음에 하루가 지나면 1 주변의 토마토가 익으면서 2 할당 되기 때문)
    return max_v - 1

M, N = map(int, input().split())
adjm = [list(map(int, input().split())) for _ in range(N)]

# 출발 지점이 2개 이상일 수 있으니
# 값이 1인 행과 열을 먼저 큐에 넣고 bfs 실행
que = deque()
for r in range(N):
    for c in range(M):
        if adjm[r][c] == 1:
            que.append((r, c))

bfs()
print(find())





