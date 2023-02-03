T = int(input())

for t in range (1, T+1) :
    nlist = []
    N, K = map(int,input().split())
    num = list(map(int,input().split()))
    
    for n in range (1, N+1) :
        if n not in num :
            nlist.append(n)

    print(f"#{t}", *nlist)