
T = int(input())

for a in range(T):
    N, M = map(int, input().split())
    aa = [list(map(int, input().split())) for i in range(N)]

    death = []
  
    for i in range(N-M+1):
        for j in range(N-M+1):
            fly = 0
            
            for k in range(M):
                for l in range(M):
                    fly += aa[i+k][j+l]
            death.append(fly)

    print("#"+str(a+1), max(death))