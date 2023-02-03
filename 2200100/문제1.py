T = int(input())
for t in range(T):
    a , b = map(int,input().split())
    student = list(range(1,a+1))
    homework = list(map(int,input().split()))
    student_homework =[]
    for i in student:
        if i not in homework :
            student_homework.append(i)    
    c = ""
    for j in student_homework:
        c += str(j)
        c += " "        
    print(f'#{t+1} {c}')