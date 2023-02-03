T = int(input())
for _ in range(T):
    N, K = map(int,input().split())
    submit = list(map(int,input().split()))
    students = [i for i in range(1,N+1)]; not_submit = []
    for i in range(N):
        if students[i] not in submit: not_submit.append(students[i])
        elif students[i] in submit: pass
    print("#{}".format(_+1), end = " ")
    for i in range(len(not_submit)): print(not_submit[i], end = " ")
    print()