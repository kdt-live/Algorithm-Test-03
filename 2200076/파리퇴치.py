import heapq

T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    # 파리채에 죽은 수를 모두 담을 리스트
    fly_death = []

    # 현재 인덱스 기준으로 오른쪽+2, 아래+2의 파리 수를 더하는 for문
    # 파리채가 인덱스를 벗어나지 않도록 n-m+1로 범위 조작
    for i in range(n-m+1):
        for j in range(n-m+1):
            total = 0
            for a in range(i, i+m):
                for b in range(j, j+m):
                    total += matrix[a][b]
            
            # 최대힙을 이용해 정렬하며 값 추가
            heapq.heappush(fly_death, -total)
    
    print(f'#{t+1} {-fly_death[0]}')