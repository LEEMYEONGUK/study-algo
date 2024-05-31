N = int(input())

grade_lst = list(map(int, input().split()))

count = 0
M = 0
for i in grade_lst:
    count += 1
    if M < i:
        M = i

for i in range(count):
    grade_lst[i] = grade_lst[i] / M * 100

sum_grade = 0

for i in grade_lst:
    sum_grade += i

print(sum_grade/count)
