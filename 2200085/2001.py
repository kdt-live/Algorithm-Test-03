import sys
input = sys.stdin.readline

for t in range (int(input())):
    n, m = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range (n)]
    killed_flies = []
    
    for i in range (n-m+1):
        for j in range (n-m+1):
            killed_sum = 0

            for di in range (m):
                for dj in range (m):
                    killed_sum += flies[i+di][j+dj]
            
            killed_flies.append(killed_sum)

    print(f'#{t+1} {max(killed_flies)}')