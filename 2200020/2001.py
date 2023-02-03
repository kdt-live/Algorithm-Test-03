T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    fly_list = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    for x in range(n-m+1):
        for y in range(n-m+1):
            fly_sum = 0
            for a in range(m):
                for b in range(m):
                    fly_sum += fly_list[x+a][y+b]
            if answer < fly_sum:
                answer = fly_sum
    print(f'#{test_case} {answer}')