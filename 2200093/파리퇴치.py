T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())

    fly = [[0] * N] * N
    catch = []
    catch_fly = []
    for j in range(N):
        fly[j] = list(map(int, input().split()))
    # print(fly)
    for k in range(N-M+1):
        for l in range(N-M+1):
            catch = []
            for m in range(M):
                for n in range(M):
                    catch.append(fly[k+m][l+n])
            
            catch_fly.append(sum(catch))

    print(f'#{i} {max(catch_fly)}')
            
