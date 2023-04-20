# 파리 퇴치

T = int(input())
for i in range(1, T + 1):
    N, M = list(map(int, input().split()))
    
    n = [[0]*N for _ in range(N)]
    for j in range(N):
        a = list(map(int, input().split()))
        n[j] = a
    
    p = []
    for k in range(N- M + 1):
        for w in range(N- M + 1):
            pari = 0
            for a in range(k, k + M):
                for b in range(w, w + M):
                    pari += n[a][b]
            p.append(pari)
    print(f'#{i} {max(p)}')