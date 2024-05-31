T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for r in range(N):
        for c in range(N):
            sr = r
            sc = c
            sum = 0

            # 배열의 모든 지점을 시작점으로
            # 파리채의 크기 만큼 순회
            for nr in range(sr, sr + M):
                for nc in range(sc, sc + M):
                    if 0 <= nr < N and 0 <= nc < N:
                        sum += arr[nr][nc]

            if max_sum < sum:
                max_sum = sum

    print(f"#{test_case} {max_sum}")
