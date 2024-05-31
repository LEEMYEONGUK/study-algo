# 국회의원 선거

N = int(input())
if N == 1:
    print(0)
else:
    one = int(input())
    result = 0
    lst = []

    for i in range(N-1):
        lst.append(int(input()))
    lst.sort(reverse=True)
    while one <= lst[0]:
        one += 1
        result += 1
        lst[0] -= 1
        lst.sort(reverse=True)
    print(result)
