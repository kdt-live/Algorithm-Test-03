# 민석이의 과제 체크하기

import sys

sys.stdin = open("input_5431.txt")
input = sys.stdin.readline

for i in range(int(input())):
    N, K = map(int, input().split())
    s = set(j for j in range(1, N + 1))
    students = set(map(int, input().split()))
    print(f"#{i + 1}", *sorted(s - students))