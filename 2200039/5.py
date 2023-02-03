from collections import deque
def password(queue):
    cnt = 1
    while True:
        if cnt <= 5:
            queue.append(queue.popleft() - cnt)
            cnt += 1
        elif cnt > 5:
            cnt = 1
            queue.append(queue.popleft() - cnt)
            cnt += 1
        if queue[-1] < 0 or queue[-1] == 0:
            queue[-1] = 0
            break
    return queue
for _ in range(10):
    test_case = int(input())
    numbers = deque(list(map(int,input().split())))
    result = list(password(numbers))
    print("#{}".format(_+1), end = " ")
    for i in range(len(result)): print(result[i], end = " ")
    print()