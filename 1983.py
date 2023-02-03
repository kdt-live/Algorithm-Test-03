#1983
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T +1):
    stu, who = map(int, input().split())
    # 높은 순서대로 점수 리스트화
    t_score = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    s_total = []

    s_sco = [list( map(int, input().split())) for _ in range(stu)]

    for S in s_sco:
        # 모든 학생들의 점수를 리스트에 넣는다
        s_total.append(S[0] * .35 + S[1] * .45 + S[2] * .2)

        # 찾고싶은 학생의 점수를 찾아 놓는다
        if S == s_sco[who - 1]:
            who_sco = S[0] * .35 + S[1] * .45 + S[2] * .2
    
    # 오름차순 정렬
    s_total = sorted(s_total, reverse = True)

    # 찾는 학생의 순위를 찾는다
    for i in range(1, stu + 1):
        if s_total[i-1] == who_sco:
            # 학생의 순위로 받을 수 있는 점수를 구한다
            for n in range(1, 11):
                if (stu / 10) * n >= i:
                    print(f"#{t} {t_score[n-1]}")
                    break