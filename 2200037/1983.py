#조교의 성적 매기기
grade_dict = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D']
test = int(input())
for T in range(1,test+1):
    n,pick = map(int,input().split())
    total = []
    for i in range(n):
        test = list(map(int,input().split()))
        total.append(test[0]*35 + test[1]*45 + test[2]*20)

    #등수 매기기
    rank_total = sorted(total,reverse=True)
    ranking = rank_total.index(total[pick-1]) + 1

    #성적 매기기

    for i in range(10):
        if i < (ranking/n *10) <= i+1:
            print(f'#{T} {grade_dict[i]}')