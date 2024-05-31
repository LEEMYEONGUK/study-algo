# 마인크래프트
import sys
input = sys.stdin.readline


N, M, B = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

min_v = 257
max_v = 0

# 최소 높이, 최대 높이 찾기
for r in range(N):
    for c in range(M):
        if min_v > arr[r][c]:
            min_v = arr[r][c]
        if max_v < arr[r][c]:
            max_v = arr[r][c]

result = [10**8, 0]

# 배열을 순회하며 목표 높이와 배열의 값에 따라 작업 횟수 추가
for h in range(min_v, max_v + 1):
    work1 = 0
    work2 = 0
    for r in range(N):
        for c in range(M):
            num = h - arr[r][c]
            # 0보다 큰 경우 블록을 더 쌓아야 하니까 2번 작업 추가
            if num > 0:
                work2 += num
            # 0보다 작은 경우 블록을 채워야 하니까 1번 작업 추가
            if num < 0:
                work1 += abs(num)

    # 작업 후 블록의 개수가 0개 이상인 경우에만 최소시간 및 해당 높이 비교
    if B - work2 + work1 >= 0:
        time = work1 * 2 + work2 * 1
        # 최소 시간 비교
        if result[0] > time:
            result[0] = time
            result[1] = h
        # 최소 시간이 같다면 높이가 더 높은 것으로 저장
        if result[0] == time:
            if result[1] < h:
                result[1] = h

print(*result)
