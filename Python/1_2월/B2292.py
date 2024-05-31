n = int(input())

if n == 1:
    print(1)

for i in range(100000):
    a = 3*((i**2) + i) + 1
    b = 3*((i**2) + (3 * i)) + 7

    if a < n <= b:
        print(i + 2)
        break
