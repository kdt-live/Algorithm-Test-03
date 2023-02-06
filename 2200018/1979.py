# 어디에 단어가 들어갈 수 있을까

import sys
sys.stdin = open("input_1979.txt")
input = sys.stdin.readline

def count_where(matrix, K: int) -> int:
    cnt = 0
    for j in matrix:
        for k in j.split("0"):
            if k == "1" * K:
                cnt += 1

    return cnt

for i in range(int(input())):
    N, K = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append(input().strip()[::2])
    
    transposed = map("".join, zip(*matrix))

    print(f"#{i + 1} {count_where(matrix, K) + count_where(transposed, K)}")