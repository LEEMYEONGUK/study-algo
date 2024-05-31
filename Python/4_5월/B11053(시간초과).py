# 가장 긴 증가하는 부분 수열
# n 선택 기회, s 선택한 횟수, tlst 부분 수열
def dfs(n, s, tlst):
    global max_v
    # 부분수열에서 값이 감소하는 경우 리턴
    if s >= 2 and tlst[s - 2] > tlst[s - 1]:
        return

    if N - n + len(tlst) < max_v:
        return
    # 최대 길이 비교
    if n == N:
        max_v = max(max_v, len(tlst))
        return
    dfs(n + 1, s, tlst)
    dfs(n + 1, s+1, tlst+[lst[n]])

N = int(input())

lst = list(map(int, input().split()))
result = []

max_v = 0
dfs(0, 0, [])

print(max_v)