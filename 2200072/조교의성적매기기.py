grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-']

t = int(input())
for case in range(1,t+1):
  n,k = map(int, input().split())
  grade_unit_num = n/10
  student_score = []
  for i in range(1,n+1):
    middle,final,project = map(int, input().split())
    score = round(middle*0.35 + final*0.45 + project*0.2)
    student_score.append((i,score))

  sort_student_score = sorted(student_score, key=lambda x :x[1], reverse=True)
  for ranking,(i,score) in enumerate(sort_student_score):
    if i == k:
      print(f'#{case}', grade[int(ranking//grade_unit_num)])
    
