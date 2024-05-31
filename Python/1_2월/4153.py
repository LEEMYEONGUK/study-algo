while True:
    num_list = list(map(int, input().split()))
    num_list.sort()
    a = num_list[0]
    b = num_list[1]
    c = num_list[2]

    if a == 0 and b == 0 and c == 0:
        break

    if a + b > c:
        if c ** 2 == a ** 2 + b ** 2:
            print("right")
        else:
            print("wrong")
    else:
        print("wrong")
