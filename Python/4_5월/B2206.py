# from collections import deque
#
# def bfs(sr, sc):
#     global result
#     q = deque([(sr, sc)])
#     visited = [[0] * M for _ in range(N)]
#     visited[sr][sc] = 1
#     while q:
#         r, c = q.popleft()
#         for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
#             nr, nc = r + dr, c + dc
#             if 0 <= nr < N and 0 <= nc < M and lst[nr][nc] == 0 and visited[nr][nc] == 0:
#                 q.append((nr, nc))
#                 visited[nr][nc] = visited[r][c] + 1
#
#     # (N-1, M-1)의 값이 0이라면 끝나는 칸에 도달하지 못한 것
#     if visited[N-1][M-1]:
#         result = min(result, visited[N-1][M-1])
#
#
# N, M = map(int, input().split())
# lst = [list(map(int, input())) for _ in range(N)]
#
# # 벽이 있는 곳의 좌표 리스트
# b_lst = []
# for r in range(N):
#     for c in range(M):
#         if lst[r][c] == 1:
#             b_lst.append((r, c))
#
# # 최단경로 비교 위한 변수 설정
# result = 10**6 + 1
# # 벽을 부수지 않고 이동
# bfs(0, 0)
# # 벽을 하나씩 부수고 이동할때
# for r, c in b_lst:
#     lst[r][c] = 0
#     bfs(0, 0)
#     lst[r][c] = 1
#
# # 최솟값이 바뀌지 않았다면 (N-1, M-1)에 도달하지 못했다는 것
# if result == 10**6 + 1:
#     print(-1)
# else:
#     print(result)


from collections import deque

# visited[r][c][0] 에는 벽을 부수지 않은 상태의 visited 값을 저장
# visited[r][c][1] 에는 벽을 부순 상태의 visited 값을 저장
def bfs():
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    while q:
        r, c, wall = q.popleft()

        if r == N-1 and c == M - 1:
            return visited[r][c][wall]

        for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc][wall] == 0:
                # 일반적인 bfs
                if lst[nr][nc] == 0:
                    q.append((nr, nc, wall))
                    visited[nr][nc][wall] = visited[r][c][wall] + 1
                # 벽을 부실 수 있으면 부수고 진행! 이때 wall에 1을 넣어서 움직이니까 또 부수지 않음!
                if wall == 0 and lst[nr][nc] == 1:
                    q.append((nr, nc, 1))
                    visited[nr][nc][1] = visited[r][c][wall] + 1
    return -1


N, M = map(int, input().split())
lst = [list(map(int, input())) for _ in range(N)]

q = deque([(0, 0, 0)])

print(bfs())