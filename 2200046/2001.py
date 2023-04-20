# 파리 퇴치

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    flies = [[0 for j in range(n)]for k in range(n)]
    result = [[0 for j in range(n - m + 1)]for k in range(n - m + 1)]

    for j in range(n):
        flies[j] = list(map(int, input().split()))

    for j in range(n - m + 1):
        for k in range(n - m + 1):
            for l in range(j, j + m):
                for o in range(k, k + m):
                    result[j][k] += flies[l][o]
    
    print(f'#{i + 1} {max(map(max, result))}')