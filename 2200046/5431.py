# 민석이의 과제 체크하기

t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    student = [True] + [False for j in range(n)]
    submit = list(map(int, input().split()))

    for number in submit:
        student[number] = True
    
    print(f'#{i + 1}', end = ' ')

    for j in range(1, n + 1):
        if not student[j]:
            print(j, end = ' ')

    print()