N = int(input())

arr = []
# arr 에 튜플 형태로 삽입
for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

# x좌표 기준으로 정렬
arr.sort()

# y좌표 기준으로 정렬
arr.sort(key=lambda x: x[1])

# arr 안에 튜플을 a,b 로 할당하여 출력
for i in range(N):
    a, b = arr[i]
    print(a, b)