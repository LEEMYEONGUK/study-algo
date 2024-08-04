# 다리 놓기

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    a, b, c = 1, 1, 1
    for i in range(1, M + 1):
        a *= i
    for i in range(1, M - N + 1):
        b *= i
    for i in range(1, N + 1):
        c *= i
    print(a // (b * c))