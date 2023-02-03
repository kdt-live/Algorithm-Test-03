
T = int(input())
for t in range(1, T+1):
    rank = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    result = []
    N, K = list(map(int,input().split()))
    for _ in range(N):
        score = list(map(int,input().split()))
        scores = score[0]*0.35 + score[1]*0.45 + score[2]*0.2
        result.append(scores)

    K_score = result[K-1]
    result.sort(reverse=True)

    K_rank = result.index(K_score)//(N//10)
    print(f'#{t} {rank[K_rank]}')