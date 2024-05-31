cnt = 0

# perm1(0) : 0번 인덱스 자리 주인 정하기
# perm1(1) : 1번 인덱스 자리 주인 정하기
# i번째 자리 주인을 정할때 i-1번째 까지 고르지 않았던 원소를 골라야 하기 때문에
# selected 배열 필요
# result => 만든 순열 들고다니기
def perm1(i, n, selected, result):
    global cnt

    # 1. 종료 조건
    # 모든 자리의 주인을 정했다면 순열 완성
    if i == n:
        cnt += 1
        print(result)
        return

    # 2. 재귀 호출
    # i번째 자리의 주인을 정하고
    # i번째 자리의 주인은 i-1번까지 선택하지 않았던 것들
    # i+1번째 자리의 주인을 정하러 가기 => 재귀호출

    for j in range(n):
        # j번 원소를 이전에 선택한 적이 없다면
        if not selected[j]:
            # j번째 원소를 i번 자리의 주인으로 놓고
            selected[j] = 1
            result[i] = arr[j]
            # i+1번째 자리의 주인을 또 선택하러 가기
            perm1(i + 1, n, selected, result)
            # j번 원소를 i번 자리의 주인으로 고려한 모든 경우의 수를 판단하고 나면
            selected[j] = 0
            # result[i] = 0


arr = [1, 2, 3, 4]
# 0번째 자리 주인부터 정하고, 길이는 4, 처음에는 아무것도 선택하지 않음
# 결과는 일단 0으로 4개 채우고 시작
perm1(0, 4, [0] * 4, [0] * 4)
print(cnt)
