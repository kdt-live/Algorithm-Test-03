T = int(input())
for t in range(1, T+1):
    a, b = map(int, input().split())
    tmp = list(map(int, input().split()))
    a = list(range(1, a+1))
    for i in tmp:
        a.remove(i)
    print(f'#{t}', *a)
    