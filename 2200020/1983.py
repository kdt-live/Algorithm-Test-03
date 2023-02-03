T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    student_score_list = []
    for i in range(n):
        mid, fin, assignment = map(int, input().split())
        student_score_list.append(round(mid*0.35 + fin*0.45 + assignment*0.2))
    student = student_score_list[k-1]
    print(f'#{test_case} {grades[sorted(student_score_list, reverse=True).index(student)*10//n]}')