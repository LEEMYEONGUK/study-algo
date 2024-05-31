N = int(input())

arr = [str(i) for i in range(1, N + 1)]

# 배열을 순회하며 "3", "6", "9"가 있을 경우 cnt 값 증가
# cnt 값을 횟수로 하여 - 출력
# "3", "6", "9" 없는 경우 숫자 그대로 출력
for i in arr:
    cnt = 0
    if "3" in i:
        cnt += i.count("3")
    if "6" in i:
        cnt += i.count("6")
    if "9" in i:
        cnt += i.count("9")
    if cnt == 0:
        arr[arr.index(i)] = i
    else:
        arr[arr.index(i)] = "-" * cnt

print(*arr)