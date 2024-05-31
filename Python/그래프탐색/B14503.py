# 로봇 청소기
from collections import deque
# 북, 동, 남, 서
dr =[-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 주의 4방향에 청소 되지 않은 빈칸 찾기
def find(r, c):
    cnt = 0
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if lst[nr][nc] == 0 and visited[nr][nc] == 0 and 0 <= nr < N and 0 <= nc < M:
            cnt += 1
    # 한 칸이라도 남아 있으면 1 리턴
    if cnt > 0:
        return 1
    # 다 청소 되어 있으면 0 리턴
    else:
        return 0

def bfs(sr, sc, sd):
    global answer
    que = deque()
    que.append((sr, sc, sd))
    while que:
        r, c, d = que.popleft()
        if visited[r][c] == 0:
            answer += 1
            visited[r][c] = 1
        # 청소되지 않은 칸이 한칸이라도 있으면
        if find(r, c):
            d -= 1
            if d == -1:
                d = 3
            nr, nc = r + dr[d], c + dc[d]
            if lst[nr][nc] == 0 and visited[nr][nc] == 0 and 0 <= nr < N and 0 <= nc < M:
                que.append((nr, nc, d))

        # 4칸 모두 청소되어 있다면
        else:
            nr, nc = r + dr[d-2], c + dc[d-2]
            if lst[nr][nc] == 0:
                que.append((nr, nc, d))
            elif lst[nr][nc] == 1 or nr < 0 or nr > N or nc < 0 or nr > M:
                break



N, M = map(int, input().split())
r, c, d = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

print(lst)
print(visited)
answer = 0
bfs(r, c, d)
print(answer)