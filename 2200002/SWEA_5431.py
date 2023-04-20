


T = int(input())

for i in range(1, i + 1):
    N, K = map(int, input().split())
    data = lsit(map(int, input().split()))
    res = []

    for j in range(1, N + 1):
        if j not in data:
            res.append(j)

    print(f'#{i}', *res)