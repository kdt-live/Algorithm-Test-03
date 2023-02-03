from collections import deque
for j in range(10):
    p = int(input())
    q = deque(list(map(int,input().split())))
    i = 1
    while True:
        if i < 6:
            l = q.popleft()
            if l - i <= 0:
                q.append(0)
                break
            else:
                q.append(l-i)
        if i>6:
            i = 0
        i+=1
    print(f"#{p}", end=' ')
    for k in range(8):
        print(q[k], end = ' ')
    print()