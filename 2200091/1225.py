import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

for _ in range(10):
    test = int(input())
    numbers = list(map(int, input().split()))
    # 앞뒤에서 삽입 삭제가 필요하니까 deque 사용
    que = deque()

    # 입력으로 들어온 수를 deque에 저장
    for num in numbers:
        que.append(num)

    # deque에서 뽑은 수에서 빼줄 수
    cnt = 1

    # 수가 0이 될 때까지 반복하기 위한 while문
    while True:
        # deque에서 수를 하나 뽑아 변수에 저장
        tmp = que.popleft()

        # 감소시킬 수가 1~5 사이면 tmp에서 빼고 다시 deque에 삽입
        # 다만 뺐을 때 0 이하라면 0을 삽입하고 while문 탈출
        if cnt < 6:
            if tmp - cnt < 1:
                que.append(0)
                break
            else:
                que.append(tmp - cnt)
            
        else:
            cnt = 1
            if tmp - cnt < 1:
                que.append(0)
                break
            else:
                que.append(tmp - cnt)
        
        cnt += 1

    print(f"#{test}", end=" ")
    print(*que)