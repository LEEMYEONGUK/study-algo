from collections import deque
def bfs():
    visited[1] = 1
    q = deque([1])
    while q:
        w = q.popleft()
        for i in adjl[w]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1

def dfs(r):
    visited[r] = 1
    for i in adjl[r]:
        if visited[i] == 0:
            dfs(i)

N = int(input())

M = int(input())
visited = [0] * (N + 1)
adjl = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)
bfs()
# or dfs(1) 실행

# print(adjl)
# print(visited)

print(sum(visited) - 1)