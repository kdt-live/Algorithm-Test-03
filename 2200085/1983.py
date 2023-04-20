for t in range (int(input())):
    n, k = map(int, input().split())
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    total = []
    total_sorted = []

    for _ in range (n):
        mid, final, assgn = map(int, input().split())
        score = (mid * 0.35) + (final * 0.45) + (assgn * 0.2)
        total.append(score)
    
    k_index = total[k-1]

    total.sort(reverse = True)

    final_score = total.index(k_index) // (n//10)
    
    print(f'#{t+1} {grades[final_score]}')