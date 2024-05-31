"""
2
4 5
WRWRW
BWRWB
WRWRW
RWBWR
6 14
WWWWWWWWWWWWWW
WWRRWWBBBBBBWW
WRRRWWWBWWWWRB
WWBWBWWWBWRRRR
WBWBBWWWBBWRRW
WWWWWWWWWWWWWW
"""
# N x M 행렬
# 위에서 몇 줄(한 줄 이상)은 모두 흰색으로
# 다음 몇 줄(한 줄 이상)은 모두 파란색으로
# 나머지 줄(한 줄 이상)은 모두 빨간색으로 칠해져야함
# 새로 칠해야 하는 칸의 개수의 최솟값?

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    # 첫줄은 무조건 흰색으로 칠하기
    # 2번째 줄에 흰색일지 파란색일지
    # 언제 파란색으로 칠하고, 언제 빨간색으로 칠할지
    # 마지막 줄은 무조건 빨간색으로 칠하기

    # 각각의 색깔이 1이상일 때의 합이 N이 되는 순열 구하기
    lst = []
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            for k in range(1, N - 1):
                if i + j + k == N:
                    lst.append([i, j, k])

    # 최솟값 비교를 위한 변수 저장
    min_cnt = 2500
    # 순열을 기반으로 x, y, z 할당
    for x, y, z in lst:
        cnt = 0
        # 각각의 범위에서 모두 흰색으로 칠하는 경우(파란색과 빨간색의 갯수)
        # 파란색으로 칠하는 경우, 빨간색으로 칠하는 경우에 새로 칠하는 횟수 cnt에 더해주기
        for i in arr[:x]:
            cnt += i.count("B") + i.count("R")
        for j in arr[x:x + y]:
            cnt += j.count("W") + j.count("R")
        for k in arr[x + y:x + y + z]:
            cnt += k.count("W") + k.count("B")
        # cnt와 최솟값 비교후 min_cnt보다 작다면 최솟값 재할당
        if min_cnt > cnt:
            min_cnt = cnt

    print(f"#{test_case} {min_cnt}")

# def white(x):
#     cnt=0
#     for i in range(m):
#         if lst[x][i]!="W":
#             cnt+=1
#     return cnt
# def blue(x):
#     cnt=0
#     for i in range(m):
#         if lst[x][i]!="B":
#             cnt+=1
#     return cnt
# def red(x):
#     cnt=0
#     for i in range(m):
#         if lst[x][i]!="R":
#             cnt+=1
#     return cnt
# t=int(input())
# for tc in range(1,t+1):
#     n,m=map(int,input().split())
#     lst=[list(map(str,input())) for _ in range(n)]
#     dp=[[51,51,51] for _ in range(n)]
#     dp[0][0]=white(0)
#     for i in range(1,n):
#         dp[i][0]=dp[i-1][0]+white(i)
#         dp[i][1]=min(dp[i-1][0],dp[i-1][1])+blue(i)
#         dp[i][2]=min(dp[i-1][1],dp[i-1][2])+red(i)
#     print(f'#{tc} {dp[n-1][2]}')

T = int(input())


# def paint(r, arr, blue, red, cnt):
#     if r == N - 2:
#         cnts.append(cnt)
#         return
#
#     if r == N - 3 and blue == False:
#         paint(r + 1, arr, True, False, cnt + M - arr[r][1])
#     else:
#         if not blue and not red:
#             paint(r + 1, arr, False, False, cnt + M - arr[r][0])
#             paint(r + 1, arr, True, False, cnt + M - arr[r][1])
#         elif blue and not red:
#             paint(r + 1, arr, True, False, cnt + M - arr[r][1])
#             paint(r + 1, arr, True, True, cnt + M - arr[r][2])
#         elif blue and red:
#             paint(r + 1, arr, True, True, cnt + M - arr[r][2])
#
#
# for t in range(1, T + 1):
#     N, M = map(int, input().split())
#     flag = [list(input()) for _ in range(N)]
#
#     const = (M - flag[0].count('W')) + (M - flag[-1].count('R'))
#
#     num_of_colors = []
#
#     for i in range(1, N - 1):
#         num_of_colors.append([flag[i].count('W'), flag[i].count('B'), flag[i].count('R')])
#
#     cnts = []
#     paint(0, num_of_colors, False, False, 0)
#
#     print(f"#{t} {const + min(cnts)}")