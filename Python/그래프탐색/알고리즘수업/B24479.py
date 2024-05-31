# 알고리즘 수업 - 깊이 우선 탐색1

# r은 시작 정점, j는 출력 순서
def dfs(r, j):
    visited[r] = 1
    order_dic[r] = j
    for i in graph[r]:
        if not visited[i]:
            dfs(i, j+1)

# 정점의 수 N, 간선의 수 M, 시작 정점 R
N, M, R = map(int, input().split())
# 그래프 정보 입력 받기
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

# 오름차순 정렬
for g in graph:
    g.sort()

# 방문 표시
visited = [0] * (N + 1)

# 출력 순서 저장
order_dic = dict()

# dfs 실행
dfs(R, 1)

# 결과 출력
for o in range(1, N + 1):
    print(order_dic.get(o, 0))