import sys
input = sys.stdin.readline

# 스택 수열
N = int(input())

stack = []
result = []
# 입력 받은 수열을 만들 수 있는 경우
find = True

# 오름차순 순서로 push
now = 1

for _ in range(N):
    num = int(input())
    # 입력 받은 수보다 push 하는 수가 작거나 같을때까지 push
    while now <= num:
        stack.append(now)
        result.append("+")
        now += 1
    # 마지막으로 push된 수가 입력 받은 수와 같다면 pop
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    # 같지 않을 경우 = 수열을 만들 수 없으니 find 값 바꿔주고 반복문 탈출
    else:
        find = False
        break

# 결과 출력
if not find:
    print("NO")
else:
    for i in result:
        print(i)