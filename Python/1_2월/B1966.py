from collections import deque

T = int(input())

def enque(x, y):
    global rear
    rear += 1
    que[rear] = (x, y)


def solve(z):
    while que:
        max_v = max(que)
        a = que.popleft()
        if a[0] == max_v[0]:
            print_order.append(a)
        else:
            que.append(a)


for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    front = -1
    rear = -1

    que = deque([0] * N)
    arr = list(map(int, input().split()))

    y = 0
    for x in arr:
        enque(x, y)
        y += 1

    print_order = []
    solve(print_order)

    for x, y in print_order:
        if y == M:
            print(print_order.index((x, y)) + 1)


# t = int(input()) #테스트 케이스 개수
# arr = []
# for _ in range(t):
#   n, m = map(int, input().split())
#   arr = list(enumerate(list(map(int, input().split()))))
#   v = arr[m]
#   idx = 0
#   while len(arr):
#     max_v = max([i[1] for i in arr])
#     if arr[0][1] == max_v:
#       now = arr.pop(0)
#       idx += 1
#       if now == v:
#         print(idx)
#         break
#     else:
#       now = arr.pop(0)
#       arr.append(now)

# enumerate()를 이용해서 문서의 중요도와 인덱스를 묶어 리스트로 만들어줬다. arr = [(0, 1), (1, 2), (2, 3), (3, 4)]
# 순서를 알고싶은 문서의 인덱스인 m을 이용해서 찾아야할 문서의 중요도와 해당 인덱스가 묶인 값을 v에 대입해줬다.
# while문을 돌면서 우선순위에 따라 대기줄을 생성했다.
# 3-1. 배열의 가장 높은 우선순위를 구해 max_v라고 하자.
# 3-2. 제일 앞에 있는 문서의 우선순위가 가장 높지 않다면, 맨 앞에서 빼고 제일 마지막에 넣어준다.
# 3-3. 제일 앞에 있는 문서의 우선순위가 가장 높다면, 해당 문서를 pop()한다. pop할 때마다 idx의 값을 1씩 증가시킨다. idx가 의미하는 것은 인쇄된 순서이다.
# 3-4. pop한 값을 v와 비교한다. 만약 v와 같으면 idx를 리턴해준다.