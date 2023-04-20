# 민석이의 과제 체크하기

T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    homework_student = list(map(int, input().split()))
    students = list(range(1, N+1))
    ans = []

    for i in students:
        if i not in homework_student:
            ans.append(i)

    print(f'#{t+1}', end=" ")
    print(*ans)         
        

