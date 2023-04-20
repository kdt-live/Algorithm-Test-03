#어디에 단어가 들어갈 수 있을까

T = int(input())
for test in range(1,T+1):
    n,x = map(int,input().split())
    cnt = 0
    x_list = [list(map(int,input().split())) for _ in range(n)]
    for i in range(n):
        cnt_x = 0
        for j in range(n):
            if x_list[i][j] == 1:
                cnt_x +=1
            else:
                if cnt_x == x:
                    cnt+=1
                    cnt_x = 0
                else:
                    cnt_x = 0
        if cnt_x == x:
            cnt+=1
        
        cnt_y = 0
        for j in range(n):
            if x_list[j][i] == 1:
                cnt_y +=1
            else:
                if cnt_y == x:
                    cnt+=1
                    cnt_y = 0
                else:
                    cnt_y = 0
        if cnt_y == x:
            cnt+=1
    print(f'#{test} {cnt}')