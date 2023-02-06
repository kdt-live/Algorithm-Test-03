


T = int(input())

for tc in range(1, T + 1):

    N, K = map(int, input().strip().split())
    score = []
    grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

    for i in range(0, N):
        mid, fin, report = map(int, input().strip().split())
        scores = round(mid * 0.35 + fin * 0.45 + report * 0.2)
        score.append(scores)

    K_score = score[K-1]
    score.sort(reverse = True)

    K_grade = int(score.index(K_score) / (N // 10))
    print("#{} {}".format(tc, grade[K_grade]))