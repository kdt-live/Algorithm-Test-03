T = int(input())
for _ in range(1,T+1):
    N, K = map(int,input().split()); matrix = []; result = 0
    for i in range(N): matrix.append(list(map(int,input().split())))
    for i in range(N):
        cnt = 0
        for j in range(N):
            if matrix[i][j] == 0:
                if cnt == K: result += 1
                cnt = 0
            else: cnt += 1
        if cnt == K: result += 1
    for j in range(N):
        cnt = 0
        for i in range(N):
            if matrix[i][j] == 0:
                if cnt == K: result += 1
                cnt = 0
            else: cnt += 1
        if cnt == K: result += 1
    print("#{} {}".format(_, result))