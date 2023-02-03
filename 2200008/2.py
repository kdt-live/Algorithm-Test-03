# 파리 퇴치
for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    space = [list(map(int, input().split())) for _ in range(n)]
    fly = []

    for i in range(n-m+1):
        for j in range(n-m+1):
            atk = 0
            for k in range(m):
                for l in range(m):
                    atk += space[i+k][j+l]
            fly.append(atk)

    print(f'#{t} {max(fly)}')