T=int(input())
for i in range (1,T+1):
    N,M=map(int,input().split())
    fly_map=[[] for _ in range (N)]
    each_fly=[]
    for j in range(N):
        fly_map[j]=list(map(int,input().split()))
    search_way=[]
    for k in range (M):
        for l in range (M):
            search_way.append((k,l))
    for m in range(N-M+1):
        for n in range(N-M+1):
            sum=0
            for o in search_way:
                a,b=o
                sum+=fly_map[m+a][n+b]
            each_fly.append(sum)
    print(f'#{i}',end=' ')
    print(max(each_fly))