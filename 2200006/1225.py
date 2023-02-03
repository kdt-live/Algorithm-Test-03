# 1225번 - [S/W 문제해결 기본] 7일차 - 암호생성기
T = 10
for _ in range(1, T  + 1):
    tc = int(input())
    num = list(map(int, input().split()))
    
    while True:
        if num[-1] <= 0:
            break

        for i in range(1, 6):
            temp = num.pop(0) - i
            if temp <= 0:
                temp = 0
            num.append(temp)
            
    print(f'#{tc}', *num)