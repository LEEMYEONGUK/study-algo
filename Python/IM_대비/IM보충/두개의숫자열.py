#두개의 숫자열의 수를 곱한 뒤 더한값의 최댓값

def solve():
    # 최댓값 저장 변수 및 곱한 뒤 더한 값 변수 저장
    max_sum = 0
    sum = 0

    # A의 길이가 B의 길이보다 더 작은 경우
    if N < M:
        # A를 한칸씩 옆으로 옮겨 계산
        for i in range(M - N + 1):
            # A의 길이만큼 반복하여 마주보는 숫자 곱해서 더하기
            for j in range(N):
                sum += A[j] * B[j + i]
            # 만약 max_sum 보다 sum이 더 클경우 재정의
            if max_sum < sum:
                max_sum = sum
            # sum 초기화
            sum = 0

    # B의 길이가 A의 길이보다 더 작 경우
    elif N > M:
        for i in range(N - M + 1):
            for j in range(M):
                sum += B[j] * A[j + i]
            if max_sum < sum:
                max_sum = sum
            sum = 0

    return max_sum

T = int(input())

for test_case in range(1, T + 1):
    # A와 B의 길이 입력
    N, M = map(int, input().split())

    # A, B 배열 입력 받기
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 결과 출력
    print(f"#{test_case} {solve()}")