# 수영장

# 2
# 10 40 100 300
# 0 0 2 9 1 5 0 0 0 0 0 0
# 10 100 50 300
# 0 0 0 0 0 0 0 0 6 2 7 8

def dfs(n, sm):
    global min_v
    if n > 13:
        return

    if n == 13:
        min_v = min(min_v, sm)
        return
    dfs(n + 1, sm + t_lst[0] * lst[n])
    dfs(n + 1, sm + t_lst[1])
    dfs(n + 3, sm + t_lst[2])
    dfs(n + 12, sm + t_lst[3])

T = int(input())

for test_case in range(1, T + 1):
    N = 12
    t_lst = list(map(int, input().split()))
    lst = [0] + list(map(int, input().split()))
    # print(t_lst)
    # print(lst)

    min_v = 1000000000
    dfs(1, 0)
    print(f'#{test_case} {min_v}')
