from collections import deque

T = 10
for t in range(T) :
    nothing = input()
    numbers = deque((map(int, input().split())))


    i = 1
    while True :
        num_front = numbers.popleft() - i
        if num_front <= 0 :
            numbers.append(0)
            break
        numbers.append(num_front)

        i += 1
        if i > 5 :
            i = 1
    print(f'#{t+1} ', end='')
    print(*numbers)