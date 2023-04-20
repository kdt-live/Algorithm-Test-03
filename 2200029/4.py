import sys
sys.stdin = open("input (2).txt", "r")

T = int(input())
for t in range(1, T + 1):
    N, k = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        length = 0
        for j in range(N):
            if matrix[i][j] == 1:
                length += 1    
            if matrix[i][j] == 0 or j == N-1:
                if length == k:
                    cnt += 1
                length = 0
        
    cnt2 = 0
    for i in range(N):
        length = 0
        for j in range(N):
            if matrix[j][i] == 1:
                length += 1
            if matrix[j][i] == 0 or j == N-1:
                if length == k:
                    cnt2 += 1
                length = 0
    print(f'#{t} {cnt + cnt2}')



