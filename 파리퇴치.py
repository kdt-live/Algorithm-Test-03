T = int(input())
for i in range(1, T+1) :
    n,m = map(int,input().split())
    s = []
    for j in range(n) :
        a = list(map(int, input().split()))
        s.append(a)
    max = 0
    for x in range(n-m+1) :
        for y in range(n-m+1) :
            cnt = 0
            for z in range(m) :
                for x in range(m) :
                    cnt +=s[x+z][y+x]
                print(cnt)
            if cnt > max :
                max = cnt 
                