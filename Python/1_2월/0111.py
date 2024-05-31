a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5, 6, 7]

mul_sum =0
mul_sum_list = []

for i in range(len(b) - len(a) + 1):
    j = 0
    for i in range(len(a)):
        mul_sum += a[i]*b[i+j]

    print(mul_sum)
    mul_sum_list.append(mul_sum)
    j += 1
print(mul_sum_list)
print(max(mul_sum_list))

print(type(len(b) - len(a) + 1))