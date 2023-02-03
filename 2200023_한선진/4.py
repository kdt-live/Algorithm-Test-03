# 파리퇴치 

T = int(input())

for t in range(1,T+1):
    a, b = list(map(int,input().split()))
    c = [[0]*a for _ in range(a)]
    for i in range(a):
        c[i] = list(map(int,input().split()))
    
    for i in range(a-b+1):
        for j in range(a-b+1):
            cnt = 0