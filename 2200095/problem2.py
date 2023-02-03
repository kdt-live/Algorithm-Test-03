# 1225. [S/W 문제해결 기본] 7일차 - 암호생성기
from collections import deque
for i in range(10):
    input()
    flag = True
    input_q = deque(map(int, input().split()))
    while flag:
        for j in range(1, 6):
            input_q.append(int(input_q.popleft()) - j)
            if input_q[7] <= 0:
                input_q[7] = 0
                print(f'#{i + 1}', end= ' ')
                print(*input_q, end='\n')

                flag = False