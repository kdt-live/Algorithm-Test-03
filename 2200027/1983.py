#조교의 성적 매기기

#총점 = 35% 45% 20%
T = int(input())

score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for test_case in range(1, T + 1):
    student, want = map(int, input().split())
    ratio = student // 10 #학점 몇명씩 줘야하는지
    score_sum = []
    for _ in range(student):
        a, b, c = map(int, input().split())
        score_sum.append((a*0.35) + (b*0.45) + (c*0.20))

    want_value = score_sum[want-1] #원하는 학생의 점수값 저장
    
    score_sum = sorted(score_sum, reverse=True) #내림차순으로 정렬

    print(f'#{test_case}', score[(score_sum.index(want_value)) // ratio])