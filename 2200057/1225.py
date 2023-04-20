import sys
from collections import deque
input = sys.stdin.readline

for _ in range(8):
    t = int(input())
    li = deque(list(map(int, input().split())))

    while li[-1] != 0:
        for i in range(1, 6):
            li.append(li.popleft() - i)
            if li[-1] < 1:
                li[-1] = 0
                break
    print(f'#{t}', end=' ')
    print(*li)