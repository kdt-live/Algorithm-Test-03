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
    a = 0
    if a<i + 1<=a+N/10 : 
        print('A+')
    a += N/10
    if a<i + 1<=a+N/10 :
        print('A0')
    a += N/10
    if a<i + 1<=a+N/10 :
        print('A-')
    a += N/10
    if a<i + 1<=a+N/10 :
        print('B+')
    a += N/10
    if a<i + 1<=a+N/10 :
        print('B0')
    a += N/10
    if a<i + 1<=a+N/10 :
        print('B-')
    a += N/10
    if a<i + 1<=a+N/10 :
        print('C+')
    a += N/10
    if a<i + 1<=a+N/10 :
        print('C0')
    a += N/10
    if a<i + 1<=a+N/10 :
        print('C-')
    a += N/10
    if a<i + 1<=a+N/10 :
        print('D0')
