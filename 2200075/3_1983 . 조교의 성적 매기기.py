T = int(input())

for t in range(1,T + 1) :
    scores = []

    N, K = map(int,input().split())
    for n in range(N) :
        score = list(map(int, input().split()))

        score = (score[0]*35/100 + score[1]*45/100 + score[2]*20/100, n+1)

        scores.append(score)

    scores = sorted(scores, reverse=True)

    for i in range(len(scores)) :
        if K == scores[i][1] :
            break
    
    print(f'#{t} ',end='')
    score_list = ['A+','A0','A-','B+','B0','B-','C+','C0','C-']
    a = 0
    for j in score_list :
        if a < i + 1 <= a + N/10 : print(j)
        a += N/10