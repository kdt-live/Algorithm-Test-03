#2 2001 파리 퇴치

t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    arr=[list(map(int,input().split())) for i in range(n)]
    max=0

    for x in range(n-m+1):
        for y in range(n-m+1):
            sum_fly=0
            for x_ in range(x,x+m):
                for y_ in range(y,y+m):
                    sum_fly+=arr[x_][y_]
            if sum_fly>max:
                max=sum_fly
            
    print(f'#{i+1} {max}')
