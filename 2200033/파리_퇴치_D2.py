T = int(input())

for i in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    max_total = 0
    for x in range(n-m+1): # 파리퇴치가 가능한 위치 찾기
        for y in range(n-m+1):

            total = 0
            for l in range(m): # 파리퇴치 몇마리 했는지
                for c in range(m):
                    total += arr[x+l][y+c]

            if max_total < total: # 파리퇴치 최고기록 저장
                max_total = total

    print(f'#{i} {max_total}')
