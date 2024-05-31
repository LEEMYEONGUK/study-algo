# 햄버거 분배

N, K = map(int, input().split())

lst = list(input())
print(lst)
result = 0
for i in range(N):
    if lst[i] == 'P':
        if 0 <= i-K and i + K + 1 <= N - 1:
            for j in range(i-K, i + K + 1):
                if lst[j] == 'H':
                    lst[j] = 'E'
                    result += 1
                    break
        elif 0 > i - K and i + K + 1 <= N-1:
            for j in range(0, i + K + 1):
                if lst[j] == 'H':
                    lst[j] = 'E'
                    result += 1
                    break
        elif 0 <= i - K and i + K + 1 > N -1:
            for j in range(i-K, N):
                if lst[j] == 'H':
                    lst[j] = 'E'
                    result += 1
                    break
print(result)

# min, max 값 활용
# n, k = map(int, input().split())
# placement = list(input())
# ans = 0
# for idx in range(n):
#     if placement[idx] == 'P':
#         for i in range(max(idx-k, 0), min(idx+k+1, n)):
#             if placement[i] == 'H':
#                 placement[i] = 0
#                 ans += 1
#                 break
# print(ans)

# 유효 범위 내의 리스트 인덱스만 접근
# for i in range(n):
#     if arr[i] == 'P':
#         for j in range(i - k, i + k + 1):
#             if -1 < j < n: # 0 <= j < n 의 조건을 만족
#                 if arr[j] == 'H':
#                     arr[j] = '-'
#                     res += 1
#                     break