import sys
sys.stdin = open("input.txt")
T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    cnt = 0
    space = 0
    for x in range(N):
        for y in range(N):
            if matrix[x][y] == 0 or y == 0:
                if cnt == K:
                    space += 1
                    cnt = 0
            elif matrix[x][y] == 1:
                cnt += 1
    cnt = 0
    for y in range(N):
        for x in range(N):
            if matrix[x][y] == 0 or x == 0:
                if cnt == K:
                    space += 1
                    cnt = 0
            elif matrix[x][y] == 1:
                cnt += 1

    print(f'#{t} {space}')
