# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    students_total = []
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    for i in range(N):
        mid, final, ass = map(int, input().split())
        total = (mid * 0.35) + (final * 0.45) + (ass * 0.20)
        students_total.append(total)
        # 74.6, 92.55000000000001, 88.8, 99.45, 72.35, 85.85000000000001, 96.25, 68.95, 85.5, 85.75

    k_score = students_total[K-1]
    # 99.45, 96.25, 92.55000000000001, 88.8, 85.85000000000001, 85.75, 85.5, 74.6, 72.35, 68.95
    rank = sorted(students_total)[::-1]

    rank_top_10 = rank.index(k_score) // (N//10)  # 2
    k_rank = grades[rank_top_10] # A-

    print(f'#{tc} {k_rank}')
