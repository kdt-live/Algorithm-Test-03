from collections import deque

for _ in range(10):
    t = int(input())
    nums = deque(map(int, input().split()))
    # minus를 1씩 증가시켜 빼기
    minus = 1

    while 1:
        n = nums.popleft() - minus
        # minus한 수가 0이하이면 0으로 바꾸고 종료
        if n < 1:
            n = 0
            nums.append(n)
            break
        nums.append(n)

        if minus == 5:
            minus = 1
        else:
            minus += 1

    print(f'#{t}', end=' ')
    print(*nums)