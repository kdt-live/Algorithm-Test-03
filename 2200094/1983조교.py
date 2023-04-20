
score = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
T = int(input())
for tc in range(1, T+1):
    score = []
    n, k = map(int, input().split())
    max = n//10 
    for idx, value in enumerate(range(n)):
        mid, fin, pro = map(int, input().split()) 
        score.append((idx + 1, (mid * 0.35 + fin * 0.45 + pro * 0.2)))
        score.sort(reverse=True, key = lambda x : x[1])
    tmp = [x[0] for x in score]  
    
    print(f"#{tc} {score[(tmp.index(k)) // max]}")