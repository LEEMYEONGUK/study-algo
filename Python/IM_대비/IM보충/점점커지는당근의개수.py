# N개의 당근을 수확하였을 때 연속으로 당근의 크기가 커진 경우 개수 출력

def solve(c):
    # 최대값 및 크기가 커진 경우의 개수
    max_cnt = 0
    cnt = 1
    for i in range(len(c) - 1):
        # 다음 당큰의 크기가 컸을 때 cnt +1
        if c[i] < c[i + 1]:
            cnt += 1
        # 당근의 크기가 같거나 작아지거나 연속으로 커지지 않았을 때
        else:
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 1
    # 마지막에 cnt 한번 더 확인
    else:
        if max_cnt < cnt:
            max_cnt = cnt

    return max_cnt

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    C = list(map(int, input().split()))
    print(f"#{test_case} {solve(C)}")

