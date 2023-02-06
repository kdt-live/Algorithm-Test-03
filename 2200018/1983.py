# 조교의 성적 매기기

import sys
sys.stdin = open("input_1983.txt")
input = sys.stdin.readline

from itertools import product

ls = product(["A", "B", "C"], ["+", "0", "-"])
ls = list(map("".join, ls)) + ["D0"]
for i in range(int(input())):
    N, K = map(int, input().split())
    scores = []
    idx = 0
    for j in range(N):
        a, b, c = map(int, input().split())
        score = a * .35 + b * .45 + c * .2
        scores.append(score)
        if j == K - 1:
            idx = score

    scores = sorted(scores, reverse=True)
    print(f"#{i + 1} {ls[scores.index(idx) // (N // 10)]}")

