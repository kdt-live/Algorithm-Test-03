T = int(input())
for t in range(1,T+1) :
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    result = []

    for i in range(1, N +1) :
        if i not in numbers :
            result.append(i)

    print(f'#{t}', end=' ')
    print(*result)

