from collections import deque
for i in range(10):
    a = input()
    l = list(map(int,input().split()))
    l = deque(l)
    
    while l[-1]!=0:
        
        for j in range(5):
            if l[0] - (j+1)<=0:
                l.popleft()
                l.append(0)
                break
            l.append(l.popleft()-(j+1))

    print(f'#{i+1}',end=' ')
    print(*l)
