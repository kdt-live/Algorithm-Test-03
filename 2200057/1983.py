import sys

input = sys.stdin.readline

T = int(input())

grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for t in range(1, T+1):
    N, K = map(int, input().split())
    li = []
    for _ in range(N):
        mid, final, hw = map(int, input().split())
        li.append(mid*0.35 + final*0.45 + hw*0.2)
    score_sorted = sorted(li, reverse=True)
    rank = score_sorted.index(li[K-1])

    print(f'#{t} {grade[(rank//(N//10))]}')