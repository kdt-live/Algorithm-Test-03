T = int(input())

for t in range(1, T+1):
    n, find = map(int, input().split())
    puzzle = [[0] * n] * n
    for l in range(n):
        puzzle[l] = list(map(int, input().split()))

    result = 0

    for i in range(n):
        cnt = 0
        for j in range(n):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or j == n-1:
                if cnt == find:
                    result += 1
        
        for j in range(n):
            if puzzle[j][i] == 1:
                cnt += 1 
            if puzzle[j][i] == 0 or j == n-1:
                if cnt == find:
                    result += 1
                cnt = 0

    print(f'#{t} {result}')