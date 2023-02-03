# 5431. 민석이의 과제 체크하기
tc = int(input())
for t in range(tc):
    N, K = map(int, input().split())
    res = [x for x in range(1, N + 1)]
    list_ = []
    list_ = list(map(int, input().split()))
    for i in list_:
        res.remove(i)
    print(f'#{t + 1}', end=' ')
    print(*res, end = '\n')