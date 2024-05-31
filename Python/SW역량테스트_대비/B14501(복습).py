# 퇴사
def dfs(n, sm):
    global max_v
    if n == N + 1:
        if max_v < sm:
            max_v = sm
        return

    if n + t_lst[n] <= N + 1:
        dfs(n + t_lst[n], sm + p_lst[n])
    dfs(n + 1, sm)

N = int(input())

t_lst = [0] * (N + 1)
p_lst = [0] * (N + 1)

for i in range(1, N + 1):
    t_lst[i], p_lst[i] = map(int, input().split())

# print(t_lst)
# print(p_lst)

max_v = 0
dfs(1, 0)
print(max_v)