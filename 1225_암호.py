from collections import deque
# import sys

# sys.stdin = open('input.txt')
# dq = deque([9550, 9556, 9550, 9553, 9558, 9551, 9551, 9551])

for _ in range(10) :
    t = int(input())
    li = list(map(int, input().split()))
    dq = deque(li)
    # print(dq)
    i = 1
    while True :   
        a = dq.popleft() - i
        if a <= 0 :
            a = 0
            dq.append(a)
            break
        dq.append(a)
        # print(a)
        # print(i)
        # 
    
        if i != 5 :
            i += 1
        else :
            i = 1    

    print(f'#{t}', end=" ")    
    print(*dq)    