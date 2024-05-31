# 톱니바퀴
from collections import deque

def left(lst):
    lst.append(lst.popleft())

def right(lst):
    lst.appendleft(lst.pop())


lst1 = deque(list(map(int, input())))
lst2 = deque(list(map(int, input())))
lst3 = deque(list(map(int, input())))
lst4 = deque(list(map(int, input())))

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    if a == 1:
        if b == 1:
            right(lst1)
        else:
            left(lst1)