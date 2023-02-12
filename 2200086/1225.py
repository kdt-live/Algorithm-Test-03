# 암호생성기

from collections import deque

for _ in range(10):
    T = int(input())
    data = deque(map(int, input().split()))
    data2 = True
    while data2:
        for i in range(1, 6):
            a = True
            num = data.popleft() - i
            if num > 0:
                data.append(num)
                data2 = True
            else:
                data.append(0)
                data2 = False
                break

    print(f'#{T}', *data)