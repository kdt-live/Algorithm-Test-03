T = int(input())

for i in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    hap_list = []
    result = 0
    result1 = 0

    for a in range(len(puzzle)):
        hap = 0
        for b in range(len(puzzle)):
            if puzzle[a][b] == 0:
                if hap == K:
                    result += 1
                hap = 0
            else:
                hap += 1
        if hap == K:
            result += 1

    for b in range(len(puzzle)):
        hap = 0
        for a in range(len(puzzle)):
            if puzzle[a][b] == 0:
                if hap == K:
                    result += 1
                hap = 0
            else:
                hap += 1
        if hap == K:
            result += 1   

    print(f'#{i} {result}')





# 아래 코드는 처음에 문제 잘못 이해하고 가로, 세로 다 누울 수 있을 때만 출력할 수 있는 코드를 짠 나
# 자체 하드모드on 했지만 결국 해낸게 뿌듯한 나
T = int(input())

for i in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    hap_list = []
    result = 0

    for a in range(len(puzzle)):
        hap = 0
        hap1 = 0
        for b in range(len(puzzle)):
            if puzzle[a][b] == 1:
                hap += 1
                for c in range(a, len(puzzle)):
                    if puzzle[c][b] == 1:
                        hap1 += 1
                        if hap1 == K:
                            hap_list.append((hap1, (a, b)))
                            hap1 = 0
                            break
                    else:
                        hap1 = 0

            else:
                hap = 0
            
        if hap >= hap_list[a][0]:
            result += 1

    print(result)
