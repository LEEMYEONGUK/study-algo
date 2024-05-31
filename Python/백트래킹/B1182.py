# 부분 수열의 합

# def dfs(n, s, l_sum, t_lst):
#     global cnt
#     if l_sum == M and n > 0:
#         print(t_lst)
#         cnt += 1
#         return
#     if n == N:
#         return
#     for j in range(s, N):
#         dfs(n + 1, j + 1, l_sum + lst[j], t_lst +[lst[j]])
#
# N, M = map(int, input().split())
# lst = list(map(int, input().split()))
# cnt = 0
# visited=[0] * N
# dfs(0, 0, 0, [])
# print(cnt)


# def dfs(n, n_sum):
#     global cnt
#     if n_sum == M and n >= 1:
#         cnt += 1
#         return
#     if n == N:
#         return
#     dfs(n + 1, n_sum)
#     dfs(n + 1, n_sum + lst[n])
#
# N, M = map(int, input().split())
# lst = list(map(int, input().split()))
# lst.sort()
#
# cnt = 0
# dfs(0, 0)
# print(cnt)

# n이 은 선택 기회이기 때문에 다 고르지 않을 수도 있고
# 조건을 잘 생각해서 선택이 다 끝난 다음에 확인하는지 중간에 확인하는지 파악
# n 고르거나 고르지 않는 횟수, sm 부분 수열의 합, cnt 고른 횟수
def dfs(n, sm, cnt):
    global ans
    # 종료조건(n에 관련) + 정답 관련 처리
    if n == N:
        if sm == S and cnt > 0:
            ans += 1
        return
    # 하부 함수 호출
    dfs(n + 1, sm + lst[n], cnt + 1)    #포함하는 경우
    dfs(n + 1, sm, cnt)                 #포함하지 않는 경우

N, S = map(int, input().split())
lst = list(map(int, input().split()))

ans = 0
dfs(0, 0, 0)
print(ans)
