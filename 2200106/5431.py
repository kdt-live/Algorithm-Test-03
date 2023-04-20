t = int(input())
for i in range(1, t+1):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    res = [i for i in range(1, n+1) if i not in nums]
    print(f'#{i}', end=' ')
    print(*res)
