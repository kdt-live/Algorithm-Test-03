# 어디에 단어가 들어갈 수 있을까

T = int(input())
for t in range(1, T + 1):
    N, K = list(map(int, input().split()))
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    
    horizon = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
                if cnt == K:
                    horizon += 1
            else:
                cnt = 0
            
            if cnt > K:
                horizon -= 1
                cnt = 0

    vertical = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[j][i] == 1:
                cnt += 1
                if cnt == K:
                    vertical += 1
            else:
                cnt = 0
            
            if cnt > K:
                vertical -= 1
                cnt = 0

    
    print(f'#{t}', horizon + vertical)
