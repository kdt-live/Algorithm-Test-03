import sys
sys.stdin = open('input_5.txt', 'r')

from collections import deque
 
def password(q:deque):
    i = 1
    while True:
        temp = q.popleft()-i
        if temp <= 0:
            break
        q.append(temp)
        i += 1
        if i == 6:
            i = 1
    q.append(0)
 
for _ in range(10):
    t = int(input())
    d = list(map(int, input().split()))
     
    min_ = min(d)
    mm = min_//15
    d_ = deque(map(lambda x: x-(mm-1)*15 , d))
 
    password(d_)
     
    print(f'#{t}', *d_)