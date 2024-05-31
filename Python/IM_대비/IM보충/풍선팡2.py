# M x N 의 격자판에 있는 풍선을 터트리면 상하좌우의 풍선이 추가로 터진다
# 풍선에는 꽃가루가 들어있고 날릴 수 있는 꽃가루 수 중 최대값 출력

# 상, 하, 좌, 우 움직일때 행과 열의 변화량
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 지점에서 움직였을 때 판을 벗어나지 않았는지 확인
def check(nr, nc):
    if 0 <= nr < N and 0 <= nc < M:
        return True
def solve():
    # 최대 합계, 합계 변수 저장
    max_sum = 0
    sum = 0

    # 격자판의 모든 지점 탐색
    for r in range(N):
        for c in range(M):
            # 시작 지점 꽃가루 개수 더하기
            sum += arr[r][c]
            # 상, 하, 좌, 우 이동
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                # 한칸씩 이동했을 때 격자판을 벗어나지 않는지 확인
                if check(nr, nc):
                    # 이동한 지점의 꽃가루 개수 더하기
                    sum += arr[nr][nc]

            # 최대 합계보다 합계가 더 클 경우 재정의
            if max_sum < sum:
                max_sum = sum
            # 합계 초기화
            sum = 0

    return max_sum

T = int(input())

for test_case in range(1, T + 1):
    # N행 M열
    N, M = map(int, input().split())
    # 격자판 입력 받기
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 결과 출력
    print(f"#{test_case} {solve()}")