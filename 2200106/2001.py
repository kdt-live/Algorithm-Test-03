def fly(x, y):
    sum_num = 0
    for i in range(m):
        for j in range(m):
            nx = x+i
            ny = y+j
            
            if nx < n and ny < n:
                sum_num += matrix[nx][ny]
    return sum_num

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    res = []
    #print(matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            res.append(fly(i, j))
    
    print(f'#{tc} {max(res)}')
