
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input())

for i in range(1, T+1):
    N, K = map(int, input().split())
    score_l = []
    
    for _ in range(N):
        m, f, w = map(int, input().split())
        score_l.append((m*0.35) + (f*0.45) + (w*0.2))
    
    k_score = score_l[K-1] # 1

    score_l.sort(reverse=True)

    find_grade = score_l.index(k_score) // (N//10)
    
    print(f'#{i} {grade[find_grade]}')


