#2001
T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    # 이중 리스트로 받는다
    fly = [list(map(int, input().split())) for _ in range(N)]
    sum_list = []
    sum = 0

    # 행 기준으로 0 ~ n-m+1까지 반복되게
    for m in range(N - M + 1 ):
        # 열이 돌아가게
        for n in range(N - M + 1):
            # 이렇게 할 필요없이 파리테를 만들어서 지정할 수 있었을까?(과제)
            sum_list.append(sum)
            sum = 0
            # 행을 파리채 크기만큼 돌려줘
            for i in range(m, m + M):
                # 열을 파리채 크기만큼 돌려줘
                for j in range(n, n + M):
                    sum += fly[i][j]

    print(f"#{t} {max(sum_list)}")

