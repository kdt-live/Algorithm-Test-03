# 파리 퇴치
# M크기의 파리채로 N 행렬을 순회..?

T = int(input())
dx = [0, 1, 1]   # 우, 좌하, 우하
dy = [1, 0, 1]

for _ in range(1, T+1):
    N, M = map(int, input(). split())
    matrix = [list(map(int, input(). split()))for _ in range(N)]
    death = 0
    fly = []

    for x in range(N):
        for y in range(N):

            for i in range(M):
                nx = x + dx[i]
                ny = y + dy[i]
                death += matrix[nx][ny]   

                if 0 <= nx < N and 0 <= ny < N:
                    x = nx
                    y = ny    