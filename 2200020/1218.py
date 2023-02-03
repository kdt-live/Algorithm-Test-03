T = 10
for test_case in range(1, T + 1):
    n = int(input())
    bracket = input()
    while True:
        n = len(bracket)
        bracket = bracket.replace('()','')
        bracket = bracket.replace('[]','')
        bracket = bracket.replace('{}','')
        bracket = bracket.replace('<>','')
        if n == len(bracket):
            break
    print(f'#{test_case} 0') if bracket else print(f'#{test_case} 1')