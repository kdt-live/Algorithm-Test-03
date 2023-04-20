T = int(input())

for i in range(1, T+1):
    n, k = map(int, input().split())
    student_score = [list(map(int, input().split())) for _ in range(n)]
    score_list = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    score_dict = {}
    for j in range(n):
        score = student_score[j][0]*0.35 + student_score[j][1]*0.45 + student_score[j][2]*0.20 # 점수 계산해서
        score_dict[j] = score #딕셔너리에 번호-점수, key-value형태로 저장

    result = sorted(score_dict.items(), key = lambda x: x[1], reverse=True) # 점수를 기준으로 큰 순서대로 정렬해서 result에 저장

    for x in result:
        if int(x[0]) + 1 == k: # k번째 수가 몇 등인지 index를 써서 계산한 후 학점으로 변환
            print(f'#{i} {score_list[result.index(x)//(n//10)]}')