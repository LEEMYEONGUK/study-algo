# 암호 만들기
def dfs(n, cnt, tst):
    # 모든 알파벳의 사용여부를 선택한 경우
    if n == C:
        # 비밀 번호 길이, 모음 개수 >= 1, 자음 개수 >= 2
        if len(tst) == L and cnt >= 1 and L - cnt >= 2:
            ans.append(tst)
        return

    # 포함하는 경우
    dfs(n + 1, cnt + tbl[ord(lst[n])], tst+lst[n])
    # 포함하지 않는 경우
    dfs(n + 1, cnt, tst)


L, C = map(int, input().split())
lst = sorted(input().split())

# Lookup tabel(모음인 경우 1, 그 외 0일 저장되어 있는...)
tbl = [0] * 128
for ch in "aeiou":
    tbl[ord(ch)] = 1

ans = []

dfs(0, 0, "")

for st in ans:
    print(st)
