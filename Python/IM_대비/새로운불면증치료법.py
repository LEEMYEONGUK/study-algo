T = int(input())

def check_num(N):
    # 카운팅 배열을 위한 리스트 저장
    check = [0] * 10

    # N의 i배(i는 1부터 시작)
    i = 1

    # 반복 횟수를 확정지을 수 없기때문에 while 반복
    while True:
        # N의 i배를 문자열로 만들어
        # 나온 숫자에 해당하는 check 리스트의 값 1 증가

        for n in str(N * i):
            check[int(n)] += 1

        # 각 숫자가 나온 횟수
        cnt = 0
        # 리스트를 순회하며 값이 1보다 클경우 cnt 1 증가
        for c in check:
            if c >= 1:
                cnt += 1
        # cnt가 10이 될때(0~9까지 1번씩 나왔을 때) N * i 값 반환
        if cnt == 10:
            return N * i
        # 반복문 탈출하지 못했을 때 N에 곱해지는 i 증가
        i += 1


for test_case in range(1, T + 1):
    # N의 배수
    N = int(input())
    # 결과값 출력
    print(f"#{test_case} {check_num(N)}")