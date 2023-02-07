# 조교의 성적 매기기

grade_dict = {0: 'A+', 1: 'A0', 2: 'A-', 3: 'B+', 4: 'B0', 
              5: 'B-', 6: 'C+', 7: 'C0', 8: 'C-', 9: 'D0'}

t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    score = list()
    grade = [None] * n

    for j in range(n):
        midterm, final, assignment = map(int, input().split())
        temp = 0.35 * midterm + 0.45 * final + 0.2 * assignment
        score.append((temp, j))
    
    score.sort(reverse = True)
    cycle = n // 10

    for j in range(n):
        grade[score[j][1]] = grade_dict[j // cycle]
    
    print(f'#{i + 1} {grade[k - 1]}')