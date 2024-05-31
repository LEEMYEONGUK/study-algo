"""
1
5
14054
44250
02032
51204
52212
"""


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input())) for _ in range(N)]

    num_sum = 0
    # 커지는 부분
    for i in range((N+1)//2):
        for j in range((N-1)//2 - i, (N-1)//2 + i + 1):
            num_sum += arr[i][j]
    # 작아지는 부분
    for i in range((N+1)//2, N):
        for j in range((N-1)//2 - (N - i) + 1, (N-1)//2 + (N -i)):
            num_sum += arr[i][j]

    print(f"#{test_case} {num_sum}")

# 가운데 점에서 특정 횟수안에 이동할 수 있는 거리인지??

# 5 * 5 배열 N = 5
# (0,2) = (0, N // 2)
# (1, 1) (1, 2) (1, 3) (i, N //2 -i) (i,
# (2, 0) (2, 1) (2, 2) (2, 3) (2, 4)
# (3, 1) (3, 2) (3, 3)
# (4, 2)
