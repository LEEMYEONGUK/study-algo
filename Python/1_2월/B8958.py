T = int(input())

for _ in range(T):
    list_sum = 0

    result = list(map(str, input().split("X")))

    for i in result:
        if len(i) % 2 == 0:
            list_sum += (1+len(i)) * (len(i)//2)
        else:
            list_sum += (1+len(i) // 2) * len(i)
    print(list_sum)
    