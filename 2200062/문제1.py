# 민석이의 과제 체크하기

T = int(input())

for i in range(1,T+1):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    no_submit= []

    for j in range(1, N+1):

        if j not in numbers:
            no_submit.append(j)

    print(f'#{i}', *no_submit)
