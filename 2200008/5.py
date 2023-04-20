# 암호생성기
from collections import deque

while True:
    try:
        t = int(input())
        code = deque(map(int, input().split()))
        while True:
            for i in range(1, 6):
                num = code.popleft()-i
                if num < 0:
                    num = 0
                code.append(num)
                if code[7] == 0:
                    break
            if code[7] == 0:
                    break

        print(f'#{t}', end=' ')
        print(*code)
    except:
        break