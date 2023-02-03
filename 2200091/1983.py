import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

test = int(input())
grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

for i in range(test):
    stu, ans = map(int, input().split())
    # 튜플(번호, 점수)을 요소로 가지는 리스트 생성
    # 0번째 학생은 없으니까 아무런 요소를 넣고 1번부터 입력 받게끔
    score = [(0, 0)] * (stu + 1)

    for j in range(stu):
        mid, final, task = map(int, input().split())
        score[j+1] = (j+1, mid*0.35 + final*0.45 + task*0.20)

    # 내림차순으로 정렬
    score = sorted(score, key=lambda x: x[1], reverse=True)
    idx = 0

    for s, n in score:
        # 리스트에 저장된 번호가 입력으로 주어진 번호와 같으면 break
        if s == ans:
            break
        idx += 1

    print(f"#{i+1} {grade[idx//(stu//10)]}")