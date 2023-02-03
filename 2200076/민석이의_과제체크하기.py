# 1. set 이용
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    total_n = set(range(1, n+1))
    submit_n = set(map(int, input().split()))

    # 전체에서 과제 낸 사람 빼서 안낸 사람 거르기
    print(f'#{i+1}', end=' ')
    print(*sorted(list(total_n-submit_n)))



# 2. 리스트 이용(set보다 시간이 빨랐음)
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    total_n = list(range(1, n+1))
    submit_n = list(map(int, input().split()))

    print(f'#{i+1}', end=' ')
    for num in total_n:
        if num not in submit_n:
            print(num, end=' ')
    print()