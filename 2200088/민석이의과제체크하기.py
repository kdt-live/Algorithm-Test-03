T = int(input())
for t in range(1, 1+T):
    students, work_s = map(int, input().split())
    work_s_l = list(map(int, input().split()))
    students_li = list(range(1, students+1))

    students_li = set(students_li)
    work_s_l = set(work_s_l)

    non_work_student = students_li - work_s_l
    print(f'#{t}', *non_work_student)