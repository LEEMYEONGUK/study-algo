T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    if a < b :
        mul_sum = 0
        mul_sum_list = []
        for i in range(b - a +1):
            j = 0
            for i in range(a):
                mul_sum += a_list[i] * b_list[i+j]
            mul_sum_list.append(mul_sum)
            j += 1
        print('#' + str(test_case) + ' ' + str(max(mul_sum_list)))
           
        
    else:
        mul_sum = 0
        mul_sum_list = []
        for i in range(a - b +1):
            j = 0
            for i in range(b):
                mul_sum += a_list[i] * b_list[i+j]
            mul_sum_list.append(mul_sum)
            j += 1
        print('#' + str(test_case) + ' ' + str(max(mul_sum_list)))