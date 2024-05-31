# 순회만 하면 되는건지 순회 + 델타 사용해야하는 건지 정확하게 파악하기
def solve():

    k_cnt = 0
    # 행 우선 순회
    for r in range(N):
        cnt = 0
        for c in range(N):
            if arr[r][c] == 1:
                cnt += 1
            else:
                if cnt == K:
                    k_cnt += 1
                cnt = 0
        if cnt == K:
            k_cnt += 1

    # 열 우선 순회
    for c in range(N):
        cnt = 0
        for r in range(N):
            if arr[r][c] == 1:
                cnt += 1
            else:
                if cnt == K:
                    k_cnt += 1
                cnt = 0
        if cnt == K:
            k_cnt += 1

    return k_cnt

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f"#{test_case} {solve()}")
