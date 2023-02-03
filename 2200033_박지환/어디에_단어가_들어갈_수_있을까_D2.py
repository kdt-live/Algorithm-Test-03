T = int(input())

for num in range(1, T+1):
    n, k = map(int, input().split())
    n_list = [list(map(int, input().split())) for _ in range(n)]
    
    total = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if n_list[i][j] == 1: # 가로로 읽는 경우
                cnt += 1
                if cnt == k: # k 만큼 1이 이어져 있으면 total 에 1을 더하지만
                    total += 1
                elif cnt == k+1: # k + 1 만큼 1이 이어져 있으면 total 에 1을 뺀다
                    total -= 1
            else:
                cnt = 0

    for i in range(n):
        cnt = 0
        for j in range(n):
            if n_list[j][i] == 1: # 세로로 읽는 경우
                cnt += 1
                if cnt == k: # k 만큼 1이 이어져 있으면 total 에 1을 더하지만
                    total += 1
                elif cnt == k+1: # k + 1 만큼 1이 이어져 있으면 total 에 1을 뺀다
                    total -= 1
            else:
                cnt = 0

    
    print(f'#{num} {total}')