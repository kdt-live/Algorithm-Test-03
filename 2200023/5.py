# 단어

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())

    a = [[''] * N for _ in range(N)]