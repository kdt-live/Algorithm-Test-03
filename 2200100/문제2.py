T = int(input())
for t in range(1,T+1):
    N , M = map(int,input().split())
    matrix = []
    for x in range(N):
        string = list(map(int,input().split()))
        matrix.append(string)
    fly = []
    sum_fly = []
    for x in range(N):
        for y in range(N):
            fly.append(matrix[x][y])
    if sum_fly : 
        print(f'#{t} {max(sum_fly)}')