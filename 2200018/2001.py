# 파리 퇴치

import sys, pprint
sys.stdin = open("input_2001.txt")
input = sys.stdin.readline

for i in range(int(input())):
    N, M = map(int, input().split())    
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    result = []
    for j in range(N - M + 1):
        for k in range(N - M + 1):
            result.append(sum(map(lambda row: sum(row[j:j + M]), matrix[k:k + M])))
    
    print(f"#{i + 1} {max(result)}")