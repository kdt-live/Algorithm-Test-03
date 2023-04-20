for idx in range(int(input())):
  N,K = map(int,input().split())
  students = []
  for num in range(N):
    scores = list(map(int,input().split())) #중간,기말,과제
    fscore = scores[0]*0.35+scores[1]*0.45+scores[2]*0.20
    students.append((fscore,num+1,))
  students.sort()
  #점수메기기 10구간
  stud_score = []
  for s in students:
    stud_score.append(s[1])
  #print(stud_score)
  r = N//10
  level = 0 #1:D0 2: C- ... 10:A+
  for i in range(0,N,r):
    level+=1
    #print(stud_score[i:i+r])
    if K in stud_score[i:i+r]:
      break
  ans = ['D','C-','C0','C+','B-','B0','B+','A-','A0','A+']
  print(f"#{idx+1}",ans[level-1])

