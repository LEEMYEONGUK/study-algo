dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, i):
    visited[r][c] = i

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] not in alpa:
            alpa.append(board[nr][nc])
            dfs(nr, nc, i + 1)
            alpa.pop(-1)


R, C = map(int, input().split())

board = [list(input()) for _ in range(R)]
alpa = []
visited = [[0] * C for _ in range(R)]

print(board)

dfs(0, 0, 1)

max_v = 0
for r in range(R):
    for c in range(C):
        if max_v < visited[r][c]:
            max_v = visited[r][c]

print(max_v)
