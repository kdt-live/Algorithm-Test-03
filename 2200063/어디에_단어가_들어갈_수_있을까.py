T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N): # 가로 탐색
        cnt = 0
        for j in range(N):
            if j != N-1:
                if matrix[i][j] == 1:
                    cnt += 1
                else:
                    if cnt == K:
                        result += 1
                    cnt = 0
            else:
                if matrix[i][j] == 1:
                    cnt += 1
                if cnt == K:
                    result += 1
        
    for i in range(N): # 세로 탐색
        cnt = 0
        for j in range(N):
            if j != N-1:
                if matrix[j][i] == 1:
                    cnt += 1
                else:
                    if cnt == K:
                        result += 1
                    cnt = 0
            
            else:
                if matrix[j][i] == 1:
                    cnt += 1
                if cnt == K:
                    result += 1

    print(f'#{t+1} {result}')