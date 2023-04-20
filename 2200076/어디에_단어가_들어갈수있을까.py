T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    # k와 같은 크기의 블럭을 셀 변수
    k_block = 0

    # 행 순회
    for i in range(n):
        cnt = 0
        for j in range(n):
            if puzzle[i][j]:
                cnt += 1
            else:
                if cnt == k:
                    k_block += 1
                cnt = 0
        if cnt == k:
            k_block += 1

    # 열 순회
    for j in range(n):
        cnt = 0
        for i in range(n):
            if puzzle[i][j]:
                cnt += 1
            else:
                if cnt == k:
                    k_block += 1
                cnt = 0
        if cnt == k:
            k_block += 1
    
    print(f'#{t+1} {k_block}')