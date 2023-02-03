# 어디에 단어가 들어갈 수 있을까

import sys
sys.stdin = open('ex.txt')

T = int(input())
for i in range(1, T + 1):
    N, K = list(map(int, input().split()))
    puzzle = [list(map(int, input().split())) for j in range(N)]
    
    print(puzzle)