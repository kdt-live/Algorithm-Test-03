#1979
T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())

    word_puzzle = [list(map(int, input().split())) for _ in range(N)]
    row = 0
    column = 0

    # 행우선
    for i in range(N):
        cnt = 0
        cnt_list = []
        for j in range(N):
            # 해당 좌표가 비어있다면 cnt += 1
            if word_puzzle[i][j] == 1:
                cnt += 1
            else:
                # 지끔까지 쌓아온 cnt 저장
                cnt_list.append(cnt)
                cnt = 0

            # 마지막까지 돌았으면 cnt 저장            
            if j == N - 1:
                cnt_list.append(cnt)

        # cnt가 지정 칸수와 같다면 낱말을 끼울수 있다
        if K in cnt_list:
            # 같은 라인에 2개 이상 있을 수도 있으니 count 사용
            row += cnt_list.count(K)
    
    # 열 우선
    for i in range(N):
        cnt = 0
        cnt_list = []
        for j in range(N):
            if word_puzzle[j][i] == 1:
                cnt += 1

            else:
                cnt_list.append(cnt)
                cnt = 0
            
            if j == N - 1:
                cnt_list.append(cnt)
    
        if K in cnt_list:
            column += cnt_list.count(K)


    print(f"#{t} {row + column}")