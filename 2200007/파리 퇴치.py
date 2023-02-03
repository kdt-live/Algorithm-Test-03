T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    fly = []

    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for k in range(M):
                for l in range(M):
                    if i + k in range(N) and j + l in range(N):
                        total += matrix[i + k][j + l]          
            fly.append(total)
    
    max = fly[0]

    for i in fly:
        if i > max:
            max = i
    
    print(f"#{t} {max}")