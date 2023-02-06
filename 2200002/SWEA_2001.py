


T = int(input())

for tc in range(1, T + 1):
    res = 0
    N, M =map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            cnt = 0

            for k in range(i, i + M):
                for L in range(j, j + M):
                    cnt += maps[k][L]

            res = max(res, cnt)
    
    print(f'#{tc}', res)