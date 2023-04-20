import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    answer = 0
    N, M = map(int, input().split())
    flies = []
    for n in range(N):
        flies.append(list(map(int, input().split())))
    answer = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            temp = 0
            for a in range(M):
                for b in range(M):
                    temp += flies[i + a][j + b]
            if temp > answer:
                answer = temp
    print(f'#{t} {answer}')