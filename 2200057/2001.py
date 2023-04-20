import sys

input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    li = [list(map(int, input().split())) for _ in range(N)]
    kill_max = 0
    
    for i in range(N-M+1):
        for j in range(N-M+1):
            kill_now = 0
            for k in range(i, i+M):
                kill_now += sum(li[k][j:j+M])
            kill_max = max(kill_max, kill_now)
    
    
    print(f'#{t} {kill_max}')