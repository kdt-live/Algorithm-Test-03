T = int(input())

for t in range(1,1+T):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    a = 0
    lst2 = []
    for i in range(N-M+1): # 1
        for j in range(N-M+1): #  0 
            for k in range(i,M+i): # 0 1
                a += sum(lst[k][j:M+j])
            lst2.append(a)
            a = 0
    lst2.sort()
    print(f'#{t} {lst2[-1]}')

