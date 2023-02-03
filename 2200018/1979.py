# 어디에 단어가 들어갈 수 있을까

import sys
sys.stdin = open("input_1983.txt")
input = sys.stdin.readline

for i in range(int(input())):
    N, K = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append(input().strip()[::2])
    
    cnt = 0
    for j in matrix:
        for k in j.split("0"):
            if k == "1" * K:
                cnt += 1

    transposed = map("".join, zip(*matrix))
    
    for j in transposed:
        for k in j.split("0"):
            if k == "1" * K:
                cnt += 1

    print(f"#{i + 1} {cnt}")