# 첫번째 문자열 아무도 없을 때 기립박수를 하는 사람의 수
# i번째 글자(i - 1 인덱스) i - 1명 이상일 때 기립 박수를 하는 사람의 수

T = int(input())

for test_case in range(1, T + 1):
    # 기립박수 치는 사람들의 조건
    p = list(map(int, input()))

    # 기립 박수 치는 사람의 수
    s_p = 0
    # 고용 해야 하는 사람의 수 합
    s_e_p = 0

    for i in range(len(p)):
        # 0명일 때 기립 박수 하는 사람의 수
        if i == 0:
            s_p += p[i]
        # p[i] 명이 인덱스 i 가 서있는 사람(s_p)보다 작거나 같다면 기립박수 침(i != 0)
        else:
            if p[i] != 0 and s_p >= i:
                s_p += p[i]
        # 인덱스 i 보다 서있는 사람의 수가 작으면 사람을 고용해야함
            elif p[i] != 0 and s_p < i:
                # 인덱스 i 에서 서있는 사람을 수를 뺀만큼 고용
                e_p = i - s_p
                # 고용한 사람을 서있는 사람의 수에 더해주기
                s_p += e_p
                # 고용한 사람의 합
                s_e_p += e_p
                # 조건 충족 되었으니 p[i] 명도 추가
                s_p += p[i]

    print(f"#{test_case} {s_e_p}")

# T = int(input())
#
# for tc in range(1, T + 1):
#     line = list(map(int, input()))
#     answer = 0
#     margin = 0
#
#     for i in range(len(line)):
#         # 인덱스 하나 증가할 때 박수 치는 사람 추가 및 하나 빼주기
#         margin += line[i]
#         margin -= 1
#         # margin 이 0보다 작을 때 한명 고용
#         if margin < 0:
#             answer += 1
#             margin += 1
#
#     print(f"#{tc} {answer}")
