T=int(input())
for i in range(1,T+1):
    N,K=map(int,input().split())
    puzzle=[[] for _ in range(N)]
    for j in range (N):
        puzzle[j]=list(map(int,input().split()))
    cnt=0
    for k in range(N):
        start_1=0
        start_2=0
        for l in range(N):
            if puzzle[k][l]: 
                start_1+= 1
                if l==N-1 and start_1==K:
                    cnt+=1
            else:
                if start_1==K:
                    cnt+=1
                start_1=0
            if puzzle[l][k]: 
                start_2+= 1
                if l==N-1 and start_2==K:
                    cnt+=1
            else:
                if start_2==K:
                    cnt+=1
                start_2=0
    print(f'#{i}',end=' ')
    print(cnt)