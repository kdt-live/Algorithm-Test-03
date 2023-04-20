tc = int(input())
for i in range(tc):
    a,b = map(int,input().split())
    l = []
    for _ in range(a):
        l.append(list(map(int,input().split())))
    l2 = []
    for j in range(a):
        s = 0
        t = 0
        for k in range(a):
            if l[j][k] == 1:
                s+=1
            elif l[j][k] == 0:
                l2.append(s)
                s = 0

            if l[k][j] == 1:
                t+=1
            elif l[k][j] == 0:
                l2.append(t)
                t = 0
        else:
            l2.append(s)
            l2.append(t)
            s = 0
            t = 0

    print(f'#{i+1} {l2.count(b)}')