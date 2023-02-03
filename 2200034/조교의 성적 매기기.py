import sys
sys.stdin = open("input3.txt", "r")

T = int(input())    #TESTCASE
     


grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for t in range(1, T + 1):     #Testcase 반복
    N,K = map(int,input().split())  #학생수 N과 알고싶은 학생 K
    allscore = []

    for i in range(N):    #테스트케이스 당 학생 수
        a = list(map(int,input().split())) #중간 기말 숙제


        score = (a[0] * 0.35) + (a[1] * 0.45) + (a[2] * 0.2) 
        allscore.append(score)     #학생당 점수를 list에 넣는다.
       

    studentK = allscore[K - 1]      #k의 점수
    sortallscore = sorted(allscore,reverse=True) #점수리스트를 내림차순으로(높은 순으로 정렬)
    
    div = N // 10                   #학생 당 중복 가능한 평점
    KK = sortallscore.index(studentK) // div
    print(f'#{t} {grade[KK]}')
        

