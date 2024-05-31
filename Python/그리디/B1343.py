# 폴리오미노

lst = list(input()) + ["."]

# print(lst)

cnt = 0
answer = ""
for i in range(len(lst)):
    if lst[i] == "X":
        cnt += 1
    elif lst[i] == ".":
        if cnt % 2 == 1:
            print(-1)
            break
        if cnt == 2:
            answer += "BB"
            cnt = 0
        if cnt == 4:
            answer += "AAAA"
            cnt = 0
        if cnt > 4:
            answer += "AAAA" * (cnt // 4)
            answer += "BB" * ((cnt % 4) // 2)
            cnt = 0
        answer += "."
else:
    a = len(answer)
    print(answer[:a-1])