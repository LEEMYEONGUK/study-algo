# N = (행의 개수), M = (열의 개수)
import copy

N, M = map(int, input().split())

chess = [list(input()) for _ in range(N)]

lst = []

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 체스의 각 지점을 시작으로
for r in range(N + 1 - 8):
    for c in range(M + 1 - 8):
        # 색칠한 횟수
        count = 0
        # 새로운 체스판
        new_chess = copy.deepcopy(chess)

        # 각 지점에서 시작할때 아래, 옆으로 8칸씩만 확인
        for i in range(8):
            for j in range(8):

                # 기준이 되는 지점이 흰색이면 상, 하, 좌, 우가 모두 검은색이 될 수 있도록 칠하기
                if new_chess[r + i][c + j] == "W":
                    # 상하좌우 확인
                    for d in range(4):
                        nr = r + i + dr[d]
                        nc = c + j + dc[d]
                        # 시작점과 시작점 기준 8칸까지만 확인 및 바꾸기
                        if r <= nr < r + 8 and c <= nc < c + 8:
                            if new_chess[nr][nc] == "W":
                                count += 1
                                new_chess[nr][nc] = "B"

                # 기준이 되는 지점이 흰색이면 상, 하, 좌, 우가 모두 검은색이 될 수 있도록 칠하기
                else:
                    # 상하좌우 확인
                    for d in range(4):
                        nr = r + i + dr[d]
                        nc = c + j + dc[d]
                        # 시작점과 시작점 기준 8칸까지만 확인 및 바꾸기
                        if r <= nr < r + 8 and c <= nc < c + 8:
                            if new_chess[nr][nc] == "B":
                                count += 1
                                new_chess[nr][nc] = "W"
        lst.append(count)

print(min(lst))
