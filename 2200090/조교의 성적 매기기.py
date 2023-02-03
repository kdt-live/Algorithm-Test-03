credit = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'DO']
for t in range(1, int(input())+1):
    N, K = map(int, input().split())
    score = []
    
    for i in range(N): # 학생 만큼 반복
        mid, final, essay = map(int, input().split())
        total = (mid*0.35)+(final*0.45)+(essay*0.2)
        score.append(total)
        
    k_number = score[K-1] # k번째 학생의 점수
    score.sort(reverse=True) # 역순 정렬 석차 매겨야하니
    div = N//10 # 50명이 있으면 5명이 평점이 같다 식?
    grade = score.index(k_number) // div
    
    print(f'#{t} {credit[grade]}')