T = int(input())

for test_case in range(1, T + 1):
    bit = input()
    cnt = 0

    # 인덱스 0번의 값이 1인 경우 cnt 증가 0으로 초기화 되기때문
    # 만약 0이라면 바꿔줄 필요가 없으므로
    if bit[0] == "1":
        cnt += 1

    # i번째와 i + 1번째 값이 다를때 카운트 1 증가
    for i in range(len(bit) - 1):
        if bit[i] != bit[i+1]:
            cnt += 1

    # 결과 출력
    print(f"#{test_case} {cnt}")
