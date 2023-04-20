# 암호생성기

from collections import deque

for i in range(10):
    case_number = int(input())
    password = deque(map(int, input().split()))
    minus = 1

    while True:
        number = password.popleft() - minus
    
        if number <= 0:
            number = 0
            password.append(number)
            break
    
        password.append(number)
    
        if minus < 5:
            minus += 1
        else:
            minus = 1
    
    print(f'#{case_number}', end = ' ')
    print(*password)