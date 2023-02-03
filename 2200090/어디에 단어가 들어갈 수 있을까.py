for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    puzzle = []
    cnt = 0
    wct = 0  
    for _ in range(n):
        puzzle.append(list(map(int, input().split())))
    # 행 기준 
    for i in range(n):
        for j in range(n):
            if puzzle[i][j] == 1: # 1을 만나면 cnt에 더한다
                cnt += 1
            if puzzle[i][j] == 0 or j == n-1: # 0, 열 벽을 만나면 초기화
                if cnt == k: # 단어길이와 같다면 단어가 들어갈 수 있으니 횟수에 더한다
                    wct += 1
                cnt = 0
    # 열 기준
    for j in range(n):
        for i in range(n):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or i == n-1: # 0, 행 벽을 만나면 초기화
                if cnt == k:
                    wct += 1
                cnt = 0    
    print(f'#{t} {wct}')