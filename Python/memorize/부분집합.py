numbers = [i for i in range(1, 11)]

selected = [0] * 10
# selected[i] == 1 : i번 원소를 부분집합에 포함시켰다.
# selected[i] == 0 : i번 원소를 부분집합에 포함시키지 않았다.

N = 10

# 재귀함수로 부분 집합 구하기 (백트래킹 응용)

# 재귀함수  for i in range(n)
# subset(0) i = 0
# subset(1) i = 1
x = 10


# 내가 i번째 원소를 부분집합에 포함 시킬지 아닐지를 결정
# n : 집합의 원소의 개수
# selected : 내가 지금까지 고른 원소를 확인하기 위해 만든 배열
def subset(i, n, selected, subsum):
    # 0. 백트래킹을 위한 최적화 조건
    if subsum == x:
        temp = []
        for j in range(n):
            if selected[j]:
                temp.append(numbers[j])
        print(temp, subsum)
        return

    elif subsum > x:
        # 내가 지금까지 구한 부분집합의 합이 원하는 값 x 를 넘어간 경우
        # 이 이상 진행할 필요가 없다.
        return

    # 1. 종료 조건
    elif i == n:
        sub_sum = 0
        # n개의 원소에 대해서 선택을 끝냈다(부분집합에 넣을지 말지)
        temp = []
        for j in range(n):
            if selected[j]:
                sub_sum += numbers[j]
                # print(numbers[j], end=" ")
                temp.append(numbers[j])
        # print()
        # print(sub_sum)
        print(temp, sub_sum)
        return

    else:
        # 2. 재귀 호출
        # i번째 원소를 고르고 i+1 번째 원소를 고를지 말지 결정하러 가기
        selected[i] = 1
        subset(i + 1, n, selected, subsum + numbers[i])
        # i번째 원소를 고르지 않고 i+1 번쨰 원소를 고를지 말지 결정하러 가기
        selected[i] = 0
        subset(i + 1, n, selected, subsum)


# 0번부터 고르기 시작, 총 N번 고민, 골랐는지 체크할 배열, 합은 0으로 시작
subset(0, N, selected, 0)
