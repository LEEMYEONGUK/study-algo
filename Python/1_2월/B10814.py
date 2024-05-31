N = int(input())

lst = []

for _ in range(N):
    a, b = map(str, input().split())
    lst.append([int(a), b])

lst.sort(key=lambda x: x[0])

for i in lst:
    print(i[0], i[1])


# sort lamda 활용
# https://velog.io/@rockwellvinca/python-sorted-sort-key-%EC%82%AC%EC%9A%A9%EB%B2%95