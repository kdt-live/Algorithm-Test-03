T = int(input())
score_list = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
for t in range(1,T+1):
    N, K = map(int,(input().split()))
    score = []
    wanted_score = 0
    for n in range(N):
        a, b, c = map(int,input().split())
        everage_score = (a*0.35) + (b*0.45) + (c*0.2)
        score.append(everage_score)
        if (n+1) == K :
            wanted_score = everage_score
    score = sorted(score, reverse=True)
    d = score.index(wanted_score)
    d = int(d//(N/10))
    print(f'#{t} {score_list[d]}') 