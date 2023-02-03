'''1983 조교의 성적 매기기
총 10개의 평점이 있다.
[A+, AO, A-, B+, BO, B-, C+, CO, C-, DO]
[총점 = 중간고사 (35%) + 기말고사 (45%) + 과제 (20%)]
10 개의 평점을 총점이 높은 순서대로 부여하는데,
각각의 평점은 같은 비율로 부여할 수 있다.

입력으로 각각의 학생들의 중간, 기말, 과제 점수가 주어지고,
학점을 알고싶은 K 번째 학생의 번호가 주어졌을 때, K 번째 학생의 학점

[제약사항]
1. N은 항상 10의 배수이며, 10이상 100이하의 정수이다. (10 ≤ N ≤ 100)
2. K는 1 이상 N 이하의 정수이다. (1 ≤ K ≤ N)
3. K 번째 학생의 총점과 다른 학생의 총점이 동일한 경우는 입력으로 주어지지 않는다.

[입력]
입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
학생수 N, 학생의 번호 K
학생이 받은 시험 및 과제 점수

[출력]
테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)'''

'''
[총점 = 중간고사 (35%) + 기말고사 (45%) + 과제 (20%)]'''
import sys
sys.stdin = open("input.txt", "r")
from pprint import pprint

grades = ['A+', 'AO', 'A-', 'B+', 'BO', 'B-', 'C+', 'CO', 'C-', 'DO']
T = int(input())
grade_dict = {x: [] for x in grades}

for test_case in range(1, T+1):
    lst = []
    N, K = map(int,input().split())
    print(N, K)
    matrix = [ list(map(int, input().split())) for _ in range(N)]
    k_score = matrix[K][0]*35 + matrix[K][1]*45 + matrix[K][2]*20
    pprint(matrix)
    for i in range(N):
        a = matrix[i][0]*35
        b = matrix[i][1]*45
        c = matrix[i][2]*20
        score = a+b+c
        lst.append(score)
    lst = sorted(lst, reverse=True)
    rank = lst.index(k_score)
    print(rank)
    cutline = len(lst)//10
    grade = rank//cutline
    print(f'#{test_case}', grades[grade], rank//cutline, len(lst), K, k_score)

#1 A-
#2 C-
#3 C0
#4 A-
#5 C0
#6 A-
#7 C+
#8 C+
#9 B0
#10 A0