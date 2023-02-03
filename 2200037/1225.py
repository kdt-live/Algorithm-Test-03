# 암호 생성기

from collections import deque

for T in range(1,11):
    int(input())
    n_list = deque(map(int,input().split()))
    while True:
        for j in range(1,6):
            n_list[0] = n_list[0]-j
            n_list.rotate(-1)
            if n_list[7] <=0:
                n_list[7] = 0
                break
        if n_list[7] <=0:
            n_list[7] = 0
            break
    print(f'#{T} ',end='')
    print(*n_list)