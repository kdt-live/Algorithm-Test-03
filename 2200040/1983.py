# 상대평가로 주어짐 10개의 평점
# 총점 = 중간고사(35%) + 기말고사(45%) + 과제(20%)
# 높은 순서대로 부여한다.

# 학점을 알고 싶은 K번째 학생의 번호가 주어졌을 때 K 번째 학생의 학점을 출력

# N은 항상 10의 배수 N%10 == 0  / 10<= N <= 100 -> 학생수
# K는 1이상 N 이하의 정수 -> 학생의 번호
# K번 째 학생의 총점과 다른 학생의 총점이 동일한 경우는 입력으로 주어지지 않는다.
# N//10 -> 20명이면 2명까지가 최고점
# N 학생 수 / 학점을 알고 싶은 학생의 번호 K
import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

# 점수 별 학점
for t in range(1, T+1):
    N, K = list(map(int, input().split())) # 학생 수 N은 항상 10의 배수
    ans = []
    for i in range(1, N+1):
        mid, final, home = list(map(int, input().split())) # 중간 기말 과제
        score = (mid*0.35) + (final*0.45) + (home*0.2)
        ans.append(score)
    # ans에 점수 부여를 한다.
    # 해당 숫자의 값 추출
    score = ans[K-1]
    # 내림차순으로 정렬
    ans.sort(reverse=True)
    # 값에 맞게 비율 설정
    # 상위 10퍼이면 a+ , 20, 30, 40. 50. 60, 70. 80 . 90 나머지는 다
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    g_score = N//10
    #10의배수로 나눈 값으로 결과찾기
    score_index = ans.index(score)//g_score 
    print(f'#{t} {grade[score_index]}')