from collections import deque

for _ in range(1, 11):
    tc = int(input())
    password = deque(list(map(int, input().split())))
    cnt = 1

    while 1:
        if cnt > 5:
            cnt = 1
        if password[-1] <= 0:
            password[-1] = 0
            break
        password.append(password.popleft() - cnt)
        cnt += 1
    print(f'#{tc}', end=' ')
    print(*password)
        
