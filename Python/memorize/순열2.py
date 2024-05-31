arr = [1, 2, 3, 4]
cnt = 0


def perm2(i, n):
    global cnt
    # 1. 종료 조건
    if i == n:
        cnt += 1
        print(arr)
        return

    # 2. 재귀 호출
    # i번 위치의 원소와 j번 위치의 원소를 교환해서 순열 만들기
    # i == j 일경우, 자리를 바꾸지 않는다는 뜻
    for j in range(i, n):
        # i번째 원소와 j번째 원소의 자리를 교환
        arr[i], arr[j] = arr[j], arr[i]
        # i+1번째 원소의 자리도 교환하러 감
        perm2(i + 1, n)
        # 자리 원래대로 되돌려놓기
        arr[i], arr[j] = arr[j], arr[i]


perm2(0, 4)
print(cnt)
