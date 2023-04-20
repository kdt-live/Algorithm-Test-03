t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0

    for i in range(n):
        temp = 0
        for j in range(n):
            if puzzle[i][j] == 1:
                temp += 1
            else:
                if temp == k:
                    cnt += 1
                temp = 0
        if temp == k:
            cnt += 1
    for i in range(n):
        temp = 0
        for j in range(n):
            if puzzle[j][i] == 1:
                temp += 1
            else:
                if temp == k:
                    cnt += 1
                temp = 0
        if temp == k:
            cnt += 1    
    print(f'#{tc} {cnt}')