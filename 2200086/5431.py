# 민석이의 과제 체크하기

T = int(input())
for i in range(1, T + 1):
    N, K = list(map(int, input().split()))
    num = list(map(int, input().split()))
    result = []
    for j in range(1, N + 1):
        if j not in num:
            result.append(j)
    print(f'#{i}', *result)
