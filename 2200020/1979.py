T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    puzzle_list = [list(map(str, input().split())) for _ in range(n)]
    answer = 0
    for x in range(n):
        answer += ''.join(puzzle_list[x]).split('0').count('1'*k)
    transpose_puzzle_list = [list(p) for p in zip(*puzzle_list)]
    for x in range(n):
        answer += ''.join(transpose_puzzle_list[x]).split('0').count('1'*k)
    print(f'#{test_case} {answer}')