# 1979 어디에 단어가 들어갈 수 있을까
T = int(input())
for I in range(1,T+1):
    N ,M = list(map(int,input().split()))
    ls = []
    for i in range(N):
        f = list(map(int,input().split()))
        ls.append(f)
    # 가로부터
    total = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if ls[i][j] == 1:
                cnt +=1
                if cnt > M:
                    cnt = 0
            else:
                if cnt == M:
                    total +=1
                cnt = 0
        if cnt == M:
            total +=1

    for i in range(N):
        cnt = 0
        for j in range(N):
            if ls[j][i] == 1:
                cnt +=1
                if cnt > M:
                    cnt = 0
            else:
                if cnt == M:
                    total +=1
                cnt = 0
        if cnt == M:
            total +=1

    print(f'#{I}',total)