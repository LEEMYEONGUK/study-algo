# 포도주 시시가

dp = [0] * 10001
lst = [0] * 10001

N = int(input())
for i in range(N):
    lst[i] = int(input())

dp[1] = lst[1]
dp[2] = lst[1] + lst[2]

for i in range(3, N+1):
    dp[i] = max(dp[i-3] + lst[i-1] + lst[i], dp[i-2] + lst[i], dp[i - 1])

print(dp[N])