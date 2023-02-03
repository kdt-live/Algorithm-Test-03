T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    answer = set(range(1, n+1)) - set(list(map(int, input().split())))
    print(f'#{test_case}', *answer)