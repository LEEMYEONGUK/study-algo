# 5000개의 버스 정류장
# 버스 노선 N개
# i번째 버스 노선은 번호가 Ai 이상 이고 Bj 이하인 모든 정류장
# P개의 버스 정류장에 대해 몇 개의 버스 노선이 다니는지 구하기

T = int(input())

for test_case in range(1, T + 1):
    # N 개의 버스
    N = int(input())
    # 버스가 지나는 버스 정류장 체크하기 위한 카운팅 배열
    bus_stop = [0] * 5001
    # N번 반복
    for _ in range(N):
        # a번 버스정류장 부터 b번 버스 정류장 카운트 1 증가
        a, b = map(int, input().split())
        for i in range(a, b + 1):
            bus_stop[i] += 1
    # 출력할 버스 정류장 번호의 개수
    P = int(input())
    print(f"#{test_case}", end=" ")
    for _ in range(P):
        c = int(input())
        print(bus_stop[c], end=" ")
    print()

