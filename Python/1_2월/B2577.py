# B2577

A = int(input())
B = int(input())
C = int(input())

mul = A * B * C
mul_list = list(str(mul))
num_list = []
# print(mul_list)
for i in range(10):
    num_list.append(str(i))

for i in num_list:
    print(mul_list.count(i))
