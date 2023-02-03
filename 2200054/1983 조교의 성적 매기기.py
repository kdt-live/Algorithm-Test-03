import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    score_list = [] 
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for i in range(N):
        score = list(map(int, input().split()))
        score_list.append(score[0]*0.35 + score[1]*0.45 + score[2]*0.20) # 총점 계산 방식
    find_score = score_list[K-1] # 만약 9번쨰 친구라면 그 친구의 점수 위치는 index 상 8번째(index는 0부터 시작)
    score_list = sorted(score_list, reverse=True)

    answer = score_list.index(find_score)//(N//10) # 등급은 비율로 지급됨 비율 공식은 N/10
	
    print(f'#{tc} {grade[answer]}')