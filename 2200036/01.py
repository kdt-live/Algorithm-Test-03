# 민석이의 과제 체크하기

T = int(input())
for i in range(1, T + 1):
    students, submits = list(map(int,input().split()))
    members = list(map(int,input().split()))
    no_submits = ""
    for j in range(1, students + 1):
        if j not in members:
            no_submits += " "+str(j)
            
    print(f"#{i}{no_submits}")