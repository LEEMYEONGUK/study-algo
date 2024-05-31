# 한 덱 = 스페이드, 다이아몬드, 하트, 클로버 각각 A, 2~10, J, Q, K의 라벨
# 4개의 무늬 별로 13장씩 총 52장의 카드가 있는 모음
# 몇장의 카드가 더 필요한지 출력, 겹치는 카드가 있을 시 오류 출력

T = int(input())
for test_case in range(1, T + 1):
    # 스페이드, 다이아몬드, 하트, 클로버 각각 카운팅 배열 만들기
    # 0번 인덱스 고려하여 0이 14개인 배열로 만들기
    s = [0] * 14
    d = [0] * 14
    h = [0] * 14
    c = [0] * 14

    # 카드 정보 입력 받기
    infor = input()
    # 3자리씩 끊기
    # i번째 정보를 통해 각 카드 무늬에 맞는 배열에
    # [i+1:i+3]번째 값 1 증가
    for i in range(0, len(infor), 3):
        if infor[i] == "S":
            s[int(infor[i+1:i+3])] += 1
        if infor[i] == "D":
            d[int(infor[i+1:i+3])] += 1
        if infor[i] == "H":
            h[int(infor[i+1:i+3])] += 1
        if infor[i] == "C":
            c[int(infor[i+1:i+3])] += 1

    # 에러 발생 여부를 위한 변수 저장
    is_error = False
    # 각각의 종류의 배열을 순회하며 1보다 큰 값 있는지 확인
    # 1보다 크다는 것은 중복이 있다는 이야기
    for i in [s, d, h, c]:
        for j in i:
            # 중복된 카드가 있을시
            if j > 1:
                # 에러 여부 참으로 바꾸고
                is_error = True
                # 에러 메세지 출력 후 반복문 탈출
                print(f"#{test_case} ERROR")
                break
        # 에러 발생시 반복문 탈출
        if is_error:
            break
    # 에러가 발생하지 않았다면 각 종류별로 카드가 몇장씩 부족한지 출력
    if not is_error:
        print(f"#{test_case}", end=" ")
        for i in [s, d, h, c]:
            print(13 - sum(i), end=" ")
    print()

