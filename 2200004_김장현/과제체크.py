t = int(input())

for i in range(1, t+1):
    n, k = map(int, input().split())
    submit = set(map(int, input().split()))
    students = set(range(1, n+1))
    fail = list(students-submit)
    fail.sort()

    print(f'#{i}', *fail)
    