from collections import deque

for _ in range(10):
    test_case = int(input())
    queue = deque(list(map(int, input().split())))
    decrease = 1

    while True:
        pop_queue = queue.popleft() - decrease

        if pop_queue <= 0:
            queue.append(0)
            break

        queue.append(pop_queue)

        if decrease != 5:
            decrease += 1
        else:
            decrease = 1
    
    print(f'#{test_case}', *queue)