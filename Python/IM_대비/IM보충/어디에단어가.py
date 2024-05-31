# data 안에 단어가 몇 개 들어가는지 반환하는 함수
def solve():
    pass

# 함수 만들어서 문제 풀면 코드 블럭화 연습 + 함수 역할 적어주기

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    # data = [input().split() for _ in range(N)]
    data = []
    for _ in range(N):
        data.append(input().split())

