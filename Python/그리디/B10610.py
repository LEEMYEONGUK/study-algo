# 30

# 내림차순으로 정렬하여 입력 받기
N = sorted(input(), reverse=True)
# 정수로 합쳐주기
result = int("".join(N))

# 3의 배수 특징 -> 각 자리수의 합이 3의 배수면 3으로 나눠떨어짐, 각 자리의 수가 바뀌는 건 아님
# 즉, 가장 큰 수 찾으려면 내림차순으로 정렬하면 됨
# 3의 배수, 10의 배수면 수 출력 아니면 -1 출력
if result % 30 == 0:
    print(result)
else:
    print(-1)
