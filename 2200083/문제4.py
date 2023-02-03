import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    # 행 우선
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[i][j] == 1:  # 흰색
                cnt += 1
            if puzzle[i][j] == 0 or j == N-1:  # 검은색 또는 끝이고
                if cnt == K:  # 흰색 칸이 단어의 길어와 동일하면
                    total += 1  # total 변수에 더하여 대입
                cnt = 0
    # 열 우선(행과 반대로)
        for j in range(N):
            if puzzle[j][i] == 1:
                cnt += 1
            if puzzle[j][i] == 0 or j == N-1:
                if cnt == K:
                    total += 1
                cnt = 0

    print(f'#{tc} {total}')
