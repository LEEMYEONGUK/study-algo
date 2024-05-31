T = 10

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    # 열 우선 순회를 하면서
    for c in range(N):
        is_red = False
        for r in range(N):
            # N극을 만났을 때 is_red 참으로
            if arr[r][c] == 1:
                is_red = True
            # S극을 만났을 때 is_red가 참이라면 cnt 1증가 후 is_red 값 초기화
            if arr[r][c] == 2 and is_red:
                cnt += 1
                is_red = False

    print(f"#{test_case} {cnt}")
