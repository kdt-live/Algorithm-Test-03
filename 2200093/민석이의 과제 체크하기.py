T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    submit = list(map(int, input().split()))
    student = [j for j in range(1, N+1)]

    for k in range(K):
        student.remove(submit[k])
    print(f'#{i+1}', *student)