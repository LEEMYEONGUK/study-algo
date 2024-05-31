def dfs(fr, fc, br, bc):
    # (N,N)에 도착 했을 때 카운트 증가
    global cnt
    if fr > N or fc > N:
        return 

    if (fr, fc) == (N, N):
        cnt += 1
        return

    # 가로로 놓여 있을 때
    if fr == br and fc - 1 == bc:
        # 대각선 이동
        if lst[fr][fc+1] == lst[fr+1][fc] == lst[fr+1][fc+1] == 0:
            dfs(fr+1, fc+1, br, bc + 1)
        # 가로 이동
        if lst[fr][fc+1] == 0:
            dfs(fr, fc+1, br, bc+1)
    # 세로로 놓여 있을 때
    if fr - 1 == br and fc == bc:
        # 대각선 이동
        if lst[fr][fc + 1] == lst[fr + 1][fc] == lst[fr + 1][fc + 1] == 0:
            dfs(fr + 1, fc + 1, br+1, bc)

        # 세로 이동
        if lst[fr+1][fc] == 0:
            dfs(fr+1, fc, br+1, bc)

    # 대각선으로 놓여 있을 때
    if fr - 1 == br and fc - 1 == bc:
        # 대각선 이동
        if lst[fr][fc + 1] == lst[fr + 1][fc] == lst[fr + 1][fc + 1] == 0:
            dfs(fr+1, fc+1, br+1, bc+1)
        # 가로 이동
        if lst[fr][fc + 1] == 0:
            dfs(fr, fc+1, br+1, bc + 1)
        # 세로 이동
        if lst[fr + 1][fc] == 0:
            dfs(fr+1, fc, br+1, bc + 1)


N = int(input())

lst = [[1]*(N + 2)] + [[1]+list(map(int, input().split()))+[1] for _ in range(N)] +[[1] * (N + 2)]
# print(lst)
cnt = 0
dfs(1, 2, 1, 1)
print(cnt)