T = int(input())
credit = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    scores = {}

    for n in range(N):
        m_exam, f_exam, assignment = map(int, input().split())
        scores[n+1] = m_exam*.35 + f_exam*.45 + assignment*.2
    
    sort_scores = sorted(scores, key= lambda x:scores[x], reverse=True)
    K_index = sort_scores.index(K)
    N_credit = {k: list(range(i*N//10, i*N//10+N//10)) for i, k in enumerate(credit)}
    
    for k, v in N_credit.items():
        if K_index in v:
            result = k

    print(f'#{test_case} {result}')