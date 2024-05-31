# import sys
# sys.stdin = open("input.txt", "r")
# 스도쿠 검증


# 가로줄 검사
def r_check():
    # 행 우선 순회하면서
    for r in range(N):
        # 배열의 값을 인덱스로 하여 값 1 증가
        check = [0] * 10
        for c in range(N):
            check[arr[r][c]] += 1
        # 카운팅 배열의 값이 1보다 큰 경우가 중복 존재
        # False 반환
        for i in check:
            if i > 1:
                return False
    # 이상 없을 시 True 반환
    return True

# 세로줄 검사
def c_check():
    for c in range(N):
        check = [0] * 10
        for r in range(N):
            check[arr[r][c]] += 1
        for i in check:
            if i > 1:
                return False
    return True

# 3 x 3 배열 검사
def small_check():
    # 시작 위치 찾기
    for sr in range(0, N, 3):
        for sc in range(0, N, 3):
            # 시작 위치로 부터 가로 세로 3칸씩 검사
            check = [0] * 10
            for r in range(sr, sr + N//3):
                for c in range(sc, sc + N//3):
                    check[arr[r][c]] += 1
            for i in check:
                if i > 1:
                    return False
    return True


T = int(input())
for test_case in range(1, T + 1):
    N = 9
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 세가지 검사가 모두 True인 경우 1 출력
    if r_check() and c_check() and small_check() == 1:
        print(f"#{test_case} 1")
    # 하나라도 False인 경우 0 출력
    else:
        print(f"#{test_case} 0")

