import sys

input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    li = list(range(1, N+1))

    stu = list(map(int, input().split()))
    for s in stu:
        li.remove(s)
    print(f'#{t}', end=' ')
    print(*li)