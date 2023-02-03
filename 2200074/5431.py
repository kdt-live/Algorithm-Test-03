T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    submit = list(map(int, input().split()))
    no_submit = []

    for number in range(1, N+1):
        if number not in submit:
            no_submit.append(number)
    
    print(f'#{test_case}', *no_submit)