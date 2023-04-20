score = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

T = int(input())

for i in range(1,T+1):
    N, K = map(int,input().split())
    rescore = []
    for z in score:
        for _ in range(N//10):
            rescore.append(z)
    N_list = []
    wanted = 0
    for j in range(1,N+1):
        a, b, c = map(int,input().split())
        N_list.append(((a*0.35)+(b*0.45)+(c*0.2)))
        if j == K:
            wanted = (a*0.35)+(b*0.45)+(c*0.2)
    N_list = sorted(N_list,reverse=True)

    print(f'#{i}',rescore[(N_list.index(wanted))])
    

    
    
