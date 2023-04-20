a = int(input())
for i in range(a):
    e = 0
    t=0
    n, k = map(int,input().split())
    q = [0]*n
    q_1=[0]*n
    l = [0]*n
    l_1=[0]*n
    b = [[0]*n for _ in range(n)]
    for j in range(n):
        c = list(map(int,input().split()))
        for t in range(n):
            b[j][t] = c[t]
    for k_1 in range(n):
        for k_2 in range(n):
            if b[k_1][k_2] == 1:
                e+=1
                q[k_1] += 1
                if q[k_1] != 0 and e == 1:
                    q[k_1] -= 1
                    q_1[k_1] +=1
                    if q_1[k_1]>q[k_1]:
                        q[k_1]=q_1[k_1]
            elif b[k_1][k_2] == 0:
                if e == k:
                    e = 0
                elif e > k:
                    e=0 
                elif e < k:
                    e=0

    for k_3 in range(n):
        for k_4 in range(n):
            if b[k_4][k_3] == 1:
                t+=1
                l[k_3] += 1
                if l[k_3] != 0 and t == 1:
                    l[k_3] -= 1
                    l_1[k_3] +=1
                    if l_1[k_3]>l[k_3]:
                        l[k_3]=l_1[k_3]
                    elif l[k_3]==l_1[k_3]:
                        l[k_3]=l[k_3]
                    
            elif b[k_4][k_3] == 0:
                if t == k:
                    t = 0
                elif t > k:
                    t=0 
                elif t < k:
                    t=0

    print(q)
    print(l)
