T = int(input())
for t in range(T):
    matrix = []
    N, M = map(int,input().split())
    cnt = 0
    for n in range(N):
        matrix.append(list(map(int,input().split())))
    num = 0
    for x in matrix :
        check = 1
        cnt = 0
        for y in x:
            if y == 1 :
                cnt +=1
            elif y == 0 :
                cnt = 0
                check = 1
            if cnt == M and check == 1:
                num += 1
                check = 0
            if y == 1 and cnt > M and check == 0 :
                check = 1
                num -= 1      
    matrix_new = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            matrix_new[i][j] = matrix[j][i]
    for x in matrix_new :
        check = 1
        cnt = 0
        for y in x:
            if y == 1 :
                cnt +=1
            elif y == 0 :
                cnt = 0
                check = 1
            if cnt == M and check == 1:
                num += 1
                check = 0
            if y == 1 and cnt > M and check == 0 :
                check = 1
                num -= 1     
    print(f'#{t+1} {num}')
    num = 0   