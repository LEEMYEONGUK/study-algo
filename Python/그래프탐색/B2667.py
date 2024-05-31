# 단지 번호 붙이기
from collections import deque
import sys
input = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 너비 우선 탐색
def bfs(sr, sc):
    cnt = 0
    visited[sr][sc] = 1
    q = deque()
    q.append((sr, sc))
    # 큐가 빌때까지 반복
    while q:
        r, c = q.popleft()
        # 큐에서 팝할때마다 cnt 1증가 = 이동한 거리 = 같은 단지 내의 집의 수
        cnt += 1
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1 and visited[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = 1
    return cnt

N = int(input())

arr = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

lst = []

# 배열을 순회하며 bfs 실행
for r in range(N):
    for c in range(N):
        # 반환값을 lst 에 삽입
        if arr[r][c] == 1 and visited[r][c] == 0:
            lst.append(bfs(r, c))

# 단지의 수 = lst의 길이
print(len(lst))
# 오름차순 정렬 후 출력
lst.sort()
for i in range(len(lst)):
    print(lst[i])

# print(len(lst),*lst, sep="\n")
