import sys
input = sys.stdin.readline

test = int(input())

for i in range(test):
    # 수강생, 제출한 사람 수 입력받기
    total, submit = map(int, input().split())
    # 제출한 사람 번호 리스트로 입력 받기
    submit_num = list(map(int, input().split()))
    # 번호는 1부터 시작이므로 인덱스와 맞춰주기 위해 total보다 하나 많은 리스트 생성
    not_submit = [0] * (total + 1)

    # 제출한 번호 리스트를 순회하면서 제출한 번호는 요소를 1로 바꿔줌
    for n in submit_num:
        not_submit[n] = 1

    print(f"#{i+1}", end=" ")
    for j in range(1, total + 1):
        if not_submit[j] == 0:
            print(j, end=" ")

    print()