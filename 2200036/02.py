# 파리 퇴치

T = int(input())
for t in range(1, T + 1):
    a, b = list(map(int,input().split()))
    matrix = []
    for i in a:
        line = list(map(int,input().split()))
        matrix.append(line)
    total_flies = []
    x_fly = []
    y_fly = []
    for f in (0, matrix[a - b]):
        for j in (0, a - b):
            killed = matrix[f][j]