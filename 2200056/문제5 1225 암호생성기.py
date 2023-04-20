from collections import deque # pop(0)를 쓰지 않기 위해... 덱 사용!
for t in range(1, 11):

    n = int(input())
    num_list = deque(map(int, input().split())) # 덱으로 숫자 받기
    while True: # 무한루프 생성
        for i in range(1,6): # 1사이클 (-1,-2,-3,-4,-5)
            a = num_list.popleft() -i # 맨 왼쪽 값 빼주고 - i
            num_list.append(a) # i빼준거 맨 뒤에 저장

            if a <= 0: # a가 음수 or 0이면
                # 음수일 경우 0으로 만들어줘야 하니...
                num_list.pop() # 맨 끝값 빼주고
                num_list.append(0) # 0추가 해주기
                print(f"#{n}", end=" ") # 그리고 프린트 후
                print(*num_list)
                break # for 반복문 종료
        # 끝값이 0이되면 while문도 종료    
        if num_list[-1] == 0:
            break

# 이 문제는 전에 문제들에 비해 오히려 쉬웠다
# 덱을 사용할때는 리스트의 내장메소드를 못 쓰나? 싶어서 좀 헤맸는데
# 다행히 굳이 안 써도 덱으로만 충분히 풀 수 있는 문제였다.
# 굳이 헷갈린 걸 하나 쓰자면....
# break 쓰는것이 for문 안에서 한번 써주고 while에서도 한번 써줘야 하기에
# 그걸 생각하는게 이 문제에서 중요한 부분이지 않았나 조심스럽게 생각한다.