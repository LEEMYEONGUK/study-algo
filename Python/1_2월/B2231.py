n = int(input())
total = 0

for i in range(1, n + 1):
    i_list = list(str(i))
    total = 0

    for num in i_list:
        total += int(num)

    if i + total == n:
        print(i)
        break

    elif i == n:
        print(0)
