score = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

T = int(input())
for tc in range(1, T+1):
    total_score = []
    n, k = map(int, input().split())
    _max = n//10 
    for idx, value in enumerate(range(n)):
        m, f, a = map(int, input().split()) 
        total_score.append((idx + 1, (m * 0.35 + f * 0.45 + a * 0.2)))
        total_score.sort(reverse=True, key = lambda x : x[1])
    tmp = [x[0] for x in total_score] 

    
    print(f"#{tc} {score[(tmp.index(k)) // _max]}")
