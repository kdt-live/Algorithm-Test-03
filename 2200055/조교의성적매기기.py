#조교의 성적 매기기
T=int(input())
score=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
for i in range(1,T+1):
    N,K=map(int,input().split())
    all_stu=[]
    for j in range (1,N+1):
        m,f,h=map(int,input().split())
        total=0.35*m+0.45*f +0.2*h
        all_stu.append((j,total))
    all_stu.sort(key=lambda x:x[1],reverse=True)
    for k in range(N):
        if all_stu[k][0]==K:
            print(f'#{i}',end=' ')
            print(score[k//int(N/10)])