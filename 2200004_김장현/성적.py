t = int(input())

rating = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']

for i in range(1, t+1):
    n, k = map(int, input().split())
    scores = []
    for j in range(n):
        m, f, h = map(int, input().split())
        score = (0.35*m) + (0.45*f) + (0.2*h)
        scores.append(score)
    kscore = scores[(k-1)]
    scores.sort()
    rank = scores.index(kscore)
    grade= rating[(rank//(n//10))]
    print(f'#{i}', grade)
