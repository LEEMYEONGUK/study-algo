# 쉬운 최단거리

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# bfs
def bfs(sr, sc):
    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 리스트 범위 내인지, 갈 수 있는 땅인지(1), 방문하지 않은 곳인지 확인
            if 0 <= nr < n and 0 <= nc < m and lst[nr][nc] == 1 and visited[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1


# 입력 받기, visited 배열 만들기(거리 입력)
n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

# print(lst)
# print(visited)

# 목표 지점 찾아서 변수 할당
sr = 0
sc = 0
for r in range(n):
    for c in range(m):
        if lst[r][c] == 2:
            sr, sc = r, c
            break

# 너비 우선 탐색 시작
bfs(sr, sc)

# 갈 수 있는 땅 중에서 도달할 수 없는 위치 -1 넣기
for r in range(n):
    for c in range(m):
        if lst[r][c] == 1 and visited[r][c] == 0:
            visited[r][c] = -1

# 대괄호 빼고 출력
for j in range(n):
    for i in range(m):
        print(visited[j][i], end=" ")
    print()