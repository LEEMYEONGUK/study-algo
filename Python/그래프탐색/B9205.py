def bfs(sj, si, ej, ei):
    # q생성, 필요 변수 등 생성
    q = []
    v = [0] * N

    # 큐에 초기 데이터 삽입, si, sj는 v에 표시 x
    q.append((sj, si))

    while q:
        cj, ci = q.pop(0)
        if abs(cj - ej) + abs(ci - ei) <= 1000:  # 목적지 도달
            return 'happy'

        # 미방문 모든 편의점 좌표 : 범위 내인지 체크
        for i in range(N):
            if v[i] == 0:  # 미방문 편의점
                nj, ni = lst[i]
                if abs(cj - nj) + abs(ci - ni) <= 1000:  # 범위내
                    q.append((nj, ni))
                    v[i] = 1
    return 'sad'


TC = int(input())

for _ in range(TC):
    N = int(input())
    sj, si = map(int, input().split())
    lst = []
    for _ in range(N):
        tj, ti = map(int, input().split())
        lst.append((tj, ti))
    ej, ei = map(int, input().split())

    ans = bfs(sj, si, ej, ei)
    print(ans)