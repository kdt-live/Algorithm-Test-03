import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    kill = []

    for i in range(n-m+1): # 파리채 휘두를 공간을 변경(m*m)
        for j in range(n-m+1):
            fly = 0

            for k in range(m):
                for l in range(m):
                    fly += arr[i + k][j + l]  # 파리채 크기가 범위를 벗어남
            kill.append(fly)

    print(f'#{tc}', max(kill))
