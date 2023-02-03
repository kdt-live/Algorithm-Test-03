import sys
sys.stdin = open('input_2.txt', 'r')

T = int(input())

for t in range(T):
    n, m = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(n)]
    result = []
    for i in range(n-m+1):
        for j in range(n-m+1):
            sum_ = 0
            for x in range(i, i+m):
                for y in range(j, j+m):
                    sum_ += d[x][y]
            result.append(sum_)
    print(f'#{t+1} {max(result)}')