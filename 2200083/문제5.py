import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    queue = list(map(int, input().split()))
    flag = 0

    while True:
        for i in range(1, 6): # 1 ~ 5 = 1 싸이클
            n = queue.pop(0) # queue의 첫번째 값을 제거
            if n - i <= 0: # 숫자가 감소할 때, 0 또는 0보다 작으면 
                queue.append(0) # 0을 추가하고
                flag = 1 # 반복문 종료조건
                break # 프로그램 종료
            queue.append(n - i) # 그 외의 경우 n-i 한 값을 추가

        if flag:
            break
    
    print(f'#{tc}', *queue)