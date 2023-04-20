# 어디에 단어가 들어갈 수 있을까?

T = int(input())
    
for t in range(T):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    cnt, total = 0, 0

    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[i][j] == 0:
                if cnt == K:
                    total += 1
                cnt = 0
            else:
                cnt += 1
        if cnt == K:
            total += 1
        
    for j in range(N):
        cnt = 0
        for i in range(N):
            if puzzle[i][j] == 0:
                if cnt == K:
                    total += 1
                cnt = 0
            else:
                cnt += 1
        if cnt == K:
            total += 1

    print(f'#{t+1} {total}')
        


