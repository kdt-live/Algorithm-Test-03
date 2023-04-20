# 조교의 성적 매기기

T = int(input())

grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for t in range(1, T+1):
    N, K = map(int, input().split())
    totals = []

    for _ in range(N): 
        a, b, c = map(int, input().split())
        total = (a * 0.35) + (b * 0.45) + (c*0.2)
        totals.append(total)
     
    k_score = totals[K-1] # 0부터 -1
    
    totals.sort(reverse=True)  # 내림차순
    
    div = N//10
    final_k_score = totals.index(k_score) // div

    print('#{} {}'.format(t, grade[final_k_score]))
