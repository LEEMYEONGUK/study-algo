# 단조증가하는 수 : 1의 자리 방향으로 갈 수록 숫자가 커지는 것

T = int(input())

for test_case in range(1, T + 1):
    # N개의 숫자 입력 받기
    N = int(input())
    arr = list(map(int, input().split()))
    # N개의 숫자들의 곱을 저장하기 위한 리스트 저장
    num_arr = []

    # N개의 숫자들의 곱 구해서 리스트에 삽입
    for i in range(N-1):
        for j in range(i + 1, N):
            num_arr.append(arr[i] * arr[j])

    # 최댓값 비교를 위한 변수 저장
    max_v = 0
    # 숫자들의 곱 하나씩 순회하며
    for n in num_arr:
        # 각 수가 일의 자리 방향으로 갈 수록 숫자가 커지지 않는다면
        # 반복문 탈출
        for s in range(len(str(n)) - 1):
            if int(str(n)[s]) > int(str(n)[s + 1]):
                break
        # 반복문이 수행된다면 해당 되는 수와 최댓값 비교
        else:
            if max_v < n:
                max_v = n
    # 최댓값이 처음과 같다면
    # 단조증가하는 수가 없으므로 -1 출력
    if max_v == 0:
        print(f"#{test_case} -1")
    # 최댓값이 0이 아니라면 최댓값 출력
    else:
        print(f"#{test_case} {max_v}")
