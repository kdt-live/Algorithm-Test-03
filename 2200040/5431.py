# 과목의 수강생 번호 1~ N번
# 제출하지 않은 사람의 번호를 오름차순으로 출력하는 프로그램을 작성하라.
# set?

# 첫 번째 줄에는 수강생의 수를 나타내는 정수와 과제를 제출한 사람의수
# 두 번째는 과제를 제출한 사람의 번호
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    student_num, submit  = list(map(int, input().split())) # 5 2
    submit_num = list(map(int, input().split())) # 2 5 3
    # 전체 학생 수
    student = [k for k in range(1, student_num+1)]

    for j in submit_num:
        if j in student:
            student.remove(j)

    
    students = list(map(str, student)) # int -> str
    ans = ' '.join(students)
    print(f'#{t} {ans}')
