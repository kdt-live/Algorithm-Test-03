T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    result = []

    for i in range(1, N+1):
        if i not in P:
            result.append(i)
    
    result = sorted(result)

    print(f'#{t+1}', *result, sep=' ')