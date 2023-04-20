T = int(input())
for t in range(1,T+1) :

    N, M = map(int,input().split())

    matrix = [list(map(int,input().split())) for n in range(N)]

    # for y1 in range(N -M) :
    #     for x1 in range(N -M) :
    result = []
    matrix2 = [[0*y for y in range(M)] for x in range(M)]
    # pprint(matrix)
    for y1 in range(N +1 -M) :
        for x1 in range(N + 1 -M) :
            sum_mat = 0
            for y2 in range(M) :
                for x2 in range(M) : 
                    matrix2[y2][x2] = matrix[y1 + y2][x1 + x2]
            # pprint(matrix2)
            for y3 in range(M) :
                sum_mat += sum(matrix2[y3])
            result.append(sum_mat)
    print(f'#{t} {max(result)}')