# 파리퇴치

T = int(input())

for t in range(T):
    N, M = map(int, input().split()) 
    matrix = [list(map(int, input().split())) for _ in range(N)] # N X N 배열
    
    ans = 0 # 가장 큰 최종 결과갑 저장, 템프
    for i in range(N - (M-1)):
        for j in range(N - (M-1)):
            temp = 0
            for x in range(M):
                for y in range(M):
                    temp += matrix[i+x][j+y]
       
            if ans < temp:
                ans = temp

    print(f'#{t+1} {ans}') 
