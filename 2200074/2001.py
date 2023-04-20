T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    flys = []

    for i in range(N-M+1):
        for j in range(N-M+1):
            fly = []
            for n in range(M):
                for m in range(M):
                    fly.append(matrix[i+n][j+m])
            flys.append(sum(fly))
    
    flys.sort()
    print(f'#{test_case}', flys.pop())