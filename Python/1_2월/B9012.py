N = int(input())

for _ in range(N):
    arr = input()
    stack = []
    # 배열을 순회하며  "("일 경우 스택에 추가
    # ")"일 경우 스택에서 pop
    # 이때 스택이 비었다면 NO 출력하고 반복문 탈출
    for i in arr:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print("N0")
                break

    # 위 반복문이 정상적으로 수행되었을 때, 스택이 비어있으면 YES 출력
    # 스택에 값이 있다면 NO 출력
    else:
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")
