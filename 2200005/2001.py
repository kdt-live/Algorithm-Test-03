
tc = int(input())
for num in range(tc):
    a,b=map(int,input().split())
    l = []
    l2 = []
    for i in range(a):
        l.append(list(map(int,input().split())))
    
    for j in range(0,a-b+1):
        for k in range(0,a-b+1):
            total = 0
            for t in range(b):
                for p in range(b):
                    total += l[j+t][k+p]

            l2.append(total)
    print(f'#{num+1} {max(l2)}')
