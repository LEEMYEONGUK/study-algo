"""
2
ABCDE
abcde
01234
FGHIJ
fghij
AABCDD
afzz
09121
a8EWg6
P5h3kx
"""
T = int(input())

for test_case in range(1, T + 1):
    # 글자열 배열 입력 받기
    arr = [list(input()) for _ in range(5)]
    # 배열에서 열의 최대 길이 확인을 위한 변수 저장
    max_c = 0
    # 배열의 행을 순회하며 열의 최대 길이 확인
    for i in arr:
        if max_c < len(i):
            max_c = len(i)

    # 다시 한번 배열을 순회하며 열의 최대 길이까지 공백 삽입
    for i in range(len(arr)):
        if len(arr[i]) < max_c:
            for _ in range(max_c - len(arr[i])):
                arr[i].append("")

    # 결과 출력
    print(f"#{test_case}", end=" ")
    # 열 우선 순회를 통해 세로 읽기
    for c in range(max_c):
            for r in range(5):
                print(arr[r][c], end="")
    print()