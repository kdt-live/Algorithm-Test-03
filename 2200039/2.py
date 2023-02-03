T = int(input())
for _ in range(T):
    N, M = map(int,input().split()); matrix = []; fly = 0; result = []
    for i in range(N):
        line = list(map(int,input().split()))
        matrix.append(line)
    dX = 1; dY = 1
    search_cnt = 1
    x_position = 0; y_position = 0
    while search_cnt <= (N-M+1)**2:
        if x_position + (M-1) * dX <= N-1:
            if y_position + (M-1) * dY <= N-1:
                for i in range(x_position, (x_position + (M-1) * dX) + 1):
                    for j in range(y_position, (y_position + (M-1) * dY) + 1):
                        fly += matrix[i][j]
                result.append(fly)
                fly = 0
                x_position += 1
                search_cnt += 1
        else:
            x_position = 0
            y_position += 1
    print("#{} {}".format(_+1, max(result)))
    matrix.clear(); result.clear()