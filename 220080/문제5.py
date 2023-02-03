# 암호생성기
from collections import deque
import sys
sys.stdin = open('input.txt','r')


num = int(input())
num1 = list(map(int,input().split()))
q = deque(num1)

print(num1[0],num1[-1])
while 1:
    for i in range(1,6):
        q[0] = q[0]-i
        q.append(q.popleft())
        if q[-1] <= 0:
            break
    if q[-1] == [0]:
        break

print(q)
