T = int(input())
flychaezip = [] #범위당 죽인 파리의 목록


for i in range(1, T + 1):
    N,M = map(int,input().split())
    squr = [list(map(int,input().split())) for _ in range(N)] 

    for row in range(N - M + 1):
        for col in range(N - M + 1):

            killcount = 0          

            for pari in range(M): 
                for chae in range(M):
                    killcount += squr[row + pari][col + chae]

            flychaezip.append(killcount)
    print(f'#{i} {max(flychaezip)}')
    flychaezip = []

    