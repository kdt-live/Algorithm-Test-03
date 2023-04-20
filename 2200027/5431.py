#5431 . 민석이의 과제 체크하기
T = int(input())

for test_case in range(1, T + 1):
    num, submit_nums = map(int, input().split()) #수강생수, 제출수
    submit = list(map(int, input().split())) #제출한 학생들
    answer =  set([i for i in range(1, num+1)]) - set(submit)
    print(f'#{test_case}', *answer)