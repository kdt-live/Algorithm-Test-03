import sys
sys.stdin = open("input.txt", "r")

def pprint(a):
    for i in a:
        print(i)
        
T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # pprint(matrix)
    death, a, b = 0, 0, 0 
    death_ls = []
    while True:   
        for i in range(M):
            for j in range(M):
                death += matrix[i + a][j + b]
        death_ls.append(death)
        death = 0
        b += 1
        if M + b > N:
            b = 0
            a += 1
        if M + a > N:
            break
    print(f'#{t} {max(death_ls)}')
            