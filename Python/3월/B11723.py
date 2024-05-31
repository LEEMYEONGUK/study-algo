import sys
input = sys.stdin.readline

S = set()

N = int(input())

for _ in range(N):
    lst = list(input().split())

    if len(lst) == 1:
        if lst[0] == "all":
            S = {i for i in range(1, 21)}
        elif lst[0] == "empty":
            S = set()
    else:
        if lst[0] == "add":
            S.add(int(lst[1]))
        if lst[0] == "remove":
            S.discard(int(lst[1]))
        if lst[0] == "check":
            if int(lst[1]) in S:
                print(1)
            else:
                print(0)
        if lst[0] == "toggle":
            if int(lst[1]) in S:
                S.discard(int(lst[1]))
            else:
                S.add(int(lst[1]))