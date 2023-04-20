T = int(input())
for _ in range(T):
    N, K = map(int,input().split()); score = []; grade = []
    alphabet = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    for i in range(N):
        midterm_exam, final_exam, homework = map(int,input().split())
        result = midterm_exam * 0.35 + final_exam * 0.45 + homework * 0.2
        score.append((result, i+1))
    score = sorted(score, reverse=True); score_cnt = 0; alphabet_cnt = 0
    for j in range(N//(N//10)):
        for i in range(N//10):
            score[score_cnt] += tuple(alphabet[alphabet_cnt])
            score_cnt += 1
        alphabet_cnt += 1
    for i in range(len(score)):
        if score[i][1] == K:
            grade = score[i][2] + score[i][3]
            grade = "".join(grade)
            print("#{} {}".format(_+1, grade))
            break