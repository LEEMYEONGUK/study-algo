# N 킬로그램 배달, 3킬로그램 봉지와 5킬로그램 봉지에 나눠 담았을 때
# 최소 봉지 몇봉지인지? 나눠 떨어지지 않을 때, -1 출력

N = int(input())

min_num = 100000

# 5킬로그램 봉지수와 3킬로그램 봉지수를 한개씩 증가시키면서 확인
for i in range(1001):
    for j in range(1700):
        # 5킬로그램 봉지와 3킬로그램 봉지로 나눠질때 두 봉지 개수의 합 저장
        if 5 * i + 3 * j == N:
            num = i + j
            # 최소값 비교 후 반복문 탈출
            if min_num > num:
                min_num = num
            break
    # 5의 배수보다 커질 경우 반복문 탈출
    if 5 * i > N:
        break
# 처음의 최소값이 변함이 없을 때 -1 출력
if min_num == 100000:
    print(-1)
# 아니라면 봉지 수의 합 출력
else:
    print(min_num)
