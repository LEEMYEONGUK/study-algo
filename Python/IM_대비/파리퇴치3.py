# 스프레이를 한 번만 뿌려 최대한 많은 파리 잡기
# 스프레이 노즐 +형태 혹은 x형태로 분사

# 상하좌우 이동
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# 대각선 이동
drr = [-1, 1, 1, -1]
dcc = [-1, -1, 1, 1]

def solve():
    # 잡을 수 있는 파리수의 최대값 변수 저장
    max_num = 0

    # 배열을 순회하며 시작점 지정

    for r in range(N):
        for c in range(N):
            # 각 시작점에서 잡을 수 있는 파리수 변수 저장
            num = 0
            # 시작점 저장하기
            sr = r
            sc = c

            # 시작점에서 잡을 수 있는 파리수 더해주기
            num += arr[r][c]

            # 상하좌우 이동( + 형태로 분사)
            for d in range(4):
                # 중심을 시작으로 M칸의 파리 잡을 수 있으니 M-1 번 이동
                for _ in range(M - 1):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    # 배열을 벗어나지 않는지 확인하고 이동한 지점의 파리수 더해주기
                    if 0 <= nr < N and 0 <= nc < N:
                        num += arr[nr][nc]
                        # 다음 이동을 위해 r, c 재정의
                        r = nr
                        c = nc
                # 다른 방향으로 움직이기 위해 r, c를 시작점으로 재정의
                r = sr
                c = sc

            # 잡은 파리수와 최대값 비교하여 재정의
            if max_num < num:
                max_num = num

            # 대각선 이동( x 형태로 분사)
            num = arr[r][c]
            for d in range(4):
                for _ in range(M - 1):
                    nr = r + drr[d]
                    nc = c + dcc[d]

                    if 0 <= nr < N and 0 <= nc < N:
                        num += arr[nr][nc]
                        r = nr
                        c = nc
                r = sr
                c = sc

            if max_num < num:
                max_num = num
    # 최대값 반환
    return max_num

T = int(input())
for test_case in range(1, T + 1):
    # N * M 배열 입력 받기
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 최대로 잡을 수 있는 파리수 출력
    print(f"#{test_case} {solve()}")

