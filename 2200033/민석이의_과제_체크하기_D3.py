T = int(input())

for i in range(1, T+1):
    n, k = map(int, input().split())
    all_student = [i for i in range(1, n+1)]
    attend_student = list(map(int, input().split()))

    absent_student = []
    for j in range(n):
        if all_student[j] not in attend_student: # 참석한 학생에 이름이 없으면 결석한 학생이다.
            absent_student.append(all_student[j])
    
    print(f'#{i}', end = ' ')
    print(*absent_student)