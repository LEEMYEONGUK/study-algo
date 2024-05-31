# 1번 부터 N번까지 N개의 상자
# 처음에는 모두 0으로 적혀있음.
# i번의 작업을 통해 L번 상자부터 R번 상자까지 값을 i로 변경

T = int(input())

for test_case in range(1, T + 1):
    # N개의 상자, Q번 작업
    N, Q = map(int, input().split())
    # 인덱스 0 번을 고려하여 0이 N + 1개인 배열 만들기
    arr = [0] * (N + 1)
    # 작업 횟수 만큼 반복
    for i in range(1, Q + 1):
        # i번째 작업의 (a ~ b)범위의 값을 i로 만들기
        a, b = map(int, input().split())
        for j in range(a, b + 1):
            arr[j] = i
    # 결과 출력
    print(f"#{test_case}", end=" ")
    for k in arr[1:]:
        print(k, end=" ")
    print()

