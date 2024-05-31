# 경계선에서 주의
# 층이 바뀌면서 다른 모서리라서 바뀌면 안되는 상황에서도
# 위, 아래가 아닌 상하좌우로 델타가 움직이면서 바뀌어 버리는 경우가 생김


from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())

dr = [-1, 1, 0, 0, -N, N]
dc = [0, 0, -1, 1, 0, 0]

adjm = [list(map(int, input().split())) for _ in range(N * H)]

que = deque()
for y in range(N * H):
    for x in range(M):
        if adjm[y][x] == 1:
            que.append((y, x))

def bfs():
    while que:
        sr, sc = que.popleft()
        for d in range(6):
            nr = sr + dr[d]
            nc = sc + dc[d]
            if 0 <= nr < N * H and 0 <= nc < M and adjm[nr][nc] == 0:
                que.append((nr, nc))
                adjm[nr][nc] = adjm[sr][sc] + 1


def find():
    max_v = -1
    for r in range(N * H):
        for c in range(M):
            if adjm[r][c] == 0:
                return -1
            if max_v < adjm[r][c]:
                max_v = adjm[r][c]
    return max_v - 1
bfs()
print(find())