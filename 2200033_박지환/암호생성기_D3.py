from collections import deque

for _ in range(10):
    T = int(input())
    queue = deque(map(int, input().split()))

    i = 0
    while True:
        i += 1
        queue.append(queue.popleft()-i) # i는 1~5까지 커진 후 1로 돌아간다.

        if i == 5:
            i = 0

        if queue[-1] <= 0: # 맨 뒷자리의 수가 0보다 작거나 같을 때
            queue[-1] = 0 # 작은 경우 음수가 되므로 0으로 바꾼다
            print(f'#{T}', end = ' ')
            print(*queue)
            break