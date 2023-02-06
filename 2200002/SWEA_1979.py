


from collections import deque

for _ in range(10):
    T = int(input())
    list1 = deque(list(map(int, input().split())))
    cnt = 0

    while list1[-1] > 0:
        list1.rotate(-1)
        list1[-1] -= cnt % 5 + 1
        cnt += 1
    list1[-1] = 0
    print(f'#{T}', *list1)

