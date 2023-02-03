#5 1225 암호생성기
from collections import deque

for i in range(10):
    t=int(input())
    queue=deque(map(int,input().split()))
    cnt=1
    while True:
        
        queue.append(queue.popleft()-cnt)
        
        # print(queue)
        if cnt==5:
            cnt=0
        cnt+=1

        if queue[-1]<=0:
            queue[-1]=0
            print(f'#{i+1}', *queue)
            break
        
