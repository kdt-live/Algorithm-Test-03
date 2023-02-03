T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = [list(input().split()) for _ in range(N)]
    rotate_matrix = [['']*N for _ in range(N)]
    words = 0

    for y in range(N):
        for x in range(N):
            rotate_matrix[y][x] = matrix[-x-1][y]
    
    for m in matrix:
        word = ''.join(m).split('0')
        for w in word:
            if len(w) == K:
                words += 1

    for m in rotate_matrix:
        word = ''.join(m).split('0')
        for w in word:
            if len(w) == K:
                words += 1
    
    print(f'#{test_case} {words}')