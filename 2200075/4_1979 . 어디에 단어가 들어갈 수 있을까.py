T = int(input())
for t in range(T) :
    N, K = map(int, input().split())
    result = 0
    matrix = [list(map(int,input().split())) for y in range(N)]

    for y in range(N) :
        cnt = 0
        for x in range(N) :
            if matrix[y][x] == 1 :
                cnt += 1
            else : 
                if cnt == K :
                    result += 1
                cnt = 0
        if cnt == K :
            result += 1
    for x in range(N) :
        cnt = 0
        for y in range(N) :
            if matrix[y][x] == 1 :
                cnt += 1
            else : 
                if cnt == K :
                    result += 1
                cnt = 0
        if cnt == K :
            result += 1

    print(f'#{t+1} {result}')