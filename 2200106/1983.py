t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    score = [list(map(int, input().split())) for _ in range(n)]
    scoring = [0.35, 0.45, 0.2]
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    total_score = []
    
    for i in score:
        temp = 0
        for j in range(len(i)):
            temp += i[j] * scoring[j]
        total_score.append(round(temp, 2))

    target = total_score[k-1]
    total_score.sort(reverse=True)

    rat = n/10
    res = total_score.index(target) // rat
    print(f'#{tc} {grade[int(res)]}')