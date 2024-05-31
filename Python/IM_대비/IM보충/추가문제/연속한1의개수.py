# N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중 최댓값

T = int(input())
for test_case in range(1, T + 1):
    # 수열의 길이 및  수열 입력 받기
    N = int(input())
    # 1로 끝나는 경우에도 최댓값 비교를 위해 [0] 추가
    arr = list(map(int, input())) + [0]

    # 중간 카운트 cnt, 최댓값 max_cnt
    cnt = 0
    max_cnt = 0
    # 수열의 순회하며 1일 경우 cnt 1 증가
    for i in range(N + 1):
        if arr[i] == 1:
            cnt += 1
        # 0을 만났을 때 cnt 비교 및 cnt 초기화
        elif arr[i] == 0:
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 0
    print(f"#{test_case} {max_cnt}")
