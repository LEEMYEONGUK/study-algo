N = 6
lst = []

for i in range(1, N - 1):
    for j in range(1, N - 1):
        for k in range(1, N - 1):
            if i + j + k == N:
                lst.append([i, j, k])

print(lst)

for x, y, z in lst:
    arr[:x], arr[x+1:x+1+y], arr[x+y+1:x+y+z+1]