# 연산자 끼워넣기(2)

def dfs(n, result):
    global result_lst
    if n == N-1:
        result_lst.append(result)
        return

    for j in range(4):
        if cal_lst[j] > 0:
            cal_lst[j] -= 1
            if j == 0:
                dfs(n + 1, result + lst[n + 1])
            elif j == 1:
                dfs(n + 1, result - lst[n + 1])
            elif j == 2:
                dfs(n + 1, result * lst[n + 1])
            elif j == 3:
                if result < 0 < lst[n + 1]:
                    dfs(n + 1, -(result//(-lst[n+1])))
                else:
                    dfs(n + 1, result//lst[n+1])
            cal_lst[j] += 1

N = int(input())
lst = list(map(int, input().split()))
cal_lst = list(map(int, input().split()))
result_lst = []
dfs(0, lst[0])
print(max(result_lst))
print(min(result_lst))