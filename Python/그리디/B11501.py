# # 주식 ( 시간 초과 )
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N = int(input())
#
#     # 주식 가격 리스트
#     lst = list(map(int, input().split())) + [0]
#     # 구매 개수 리스트
#     buy_lst = [0] * (N + 1)
#     # 이익
#     result = 0
#
#     # for문으로 lst 순회
#     for i in range(N):
#         answer = 0
#         # 다음날 주식 가격이 떨어지면 전량 매도
#         if lst[i] > lst[i + 1]:
#             if sum(buy_lst):
#                 # 그동안 사놓았던 주식 팔기
#                 for j in range(i + 1):
#                     answer += (lst[i]-lst[j]) * buy_lst[j]
#                     # 떨어졌다가 다시 오를 수 있으니까(테케3) 팔았다는 표시
#                     buy_lst[j] = 0
#
#         # 다음날 주식 가격이 같거나 오른다면 구매하기
#         elif lst[i] <= lst[i + 1]:
#             buy_lst[i] = 1
#         # 판 금액이 0이 아니라면 result에 더해주기
#         if answer:
#             result += answer
#     print(result)

# 10 ** 12


# # 주식 # 틀림
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N = int(input())
#
#     # 주식 가격 리스트
#     # 마지막 날까지 가격이 올랐을 경우 for 순회가 끝날때 계산을 하기 위해 0 추가
#     lst = list(map(int, input().split())) + [0]
#
#     # 계속 하락장인지 확인
#     flag = 0
#     for i in range(N):
#         if lst[i] < lst[i + 1]:
#             flag = 1
#
#     if flag == 1:
#         # flag 다시 0으로 설정
#         flag = 0
#         # 이익
#         profit = 0
#         # 지금까지 산 주식의 수
#         cnt = 0
#
#         for i in range(N):
#             # 상승할 때 flag 1로 저장
#             if lst[i] < lst[i + 1]:
#                 flag = 1
#             # 다음날 주식 가격이 떨어지고 주식 가격이 상승한 적이 있었을 경우 전량 매도
#             if lst[i] > lst[i + 1] and flag:
#                 profit += lst[i] * cnt
#                 cnt = 0
#                 flag = 0
#             # 팔 때는 당일 주식 사지 않아야 함
#             else:
#                 cnt += 1
#                 profit += lst[i] * -1
#         print(profit)
#     else:
#         print(0)

# 1
# 5
# 10 7 6 10 13


# 주식

T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    lst = list(map(int, input().split()))

    # 이익
    profit = 0

    # 주식의 최대 가격
    max_price = 0

    for i in range(N-1, -1, -1):
        if lst[i] > max_price:
            max_price = lst[i]
        # 현재 가격이 현재 최대 가격보다 작다면 차익 실현
        else:
            profit += max_price - lst[i]

    print(profit)

