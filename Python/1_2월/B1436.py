# N = int(input())
#
# cnt = [0] * (N)
#
# cnt[N - 1] += 1
#
# print(int(str(cnt.index(1)) + "666"))
#
# 666
# 5666
#
# 6개
#
# 6661
#
# 6669
#
# 7666
# 15666
#
# 16660
# 16669
#
# 26660
# 26669
#
# 66600
# 66666
# 66699

N = int(input())
s_list = []

for i in range(1, 10000001):
    cnt = 0
    for s in str(i) + "0":
        if s == "6":
            cnt += 1
        else:
            if cnt >= 3:
                s_list.append(i)
                break
            else:
                cnt = 0
print(s_list[N - 1])
