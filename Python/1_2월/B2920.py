a = list(map(int, input().split()))

asc = [1, 2, 3, 4, 5, 6, 7, 8]
desc = [8, 7, 6, 5, 4, 3, 2, 1]

if a == asc:
    print("ascending")
elif a == desc:
    print("descending")
else:
    print("mixed")

# a = input()
# print(a)
# print(type(a))