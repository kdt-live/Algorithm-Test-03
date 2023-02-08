from collections import deque

for _ in range(10):
    test_case = int(input())
    numbers = list(map(int, input().split()))

    deque_numbers = deque(numbers)
    button = True
    while button:
        # 한 사이클
        for i in range(1,6):
            # deque를 이용해 첫 번째 요소를 떼어 i만큼 빼고 제일 뒷 요소로 추가한다.
            deque_numbers.append(deque_numbers.popleft() - i)

            # 맨 뒤 요소가 0과 같거나 작으면 0으로 바꿔주고 반복을 멈춘다.
            if deque_numbers[-1] <= 0:
                deque_numbers[-1] = 0
                button = False
                break
    print(f'#{test_case}',*list(deque_numbers))

# 이전 코드
# for _ in range(1):
# # for _ in range(10):
#   t = int(input())
#   numbers = list(map(int, input().split()))

#   deque_numbers = deque(numbers)
#   minus = 1
#   while True:
#     print(minus)
#     deque_numbers.append(deque_numbers.popleft() - minus)
#     # deque_numbers.popleft()
#     minus += 1
#     print(deque_numbers)
#     if deque_numbers[-1] < 0:
#       deque_numbers[-1] = 0
#       break
#   print(f'#{t}',*deque_numbers)
    
#   # 보완사항: 두번째 사이클부터 다시 minus는 1이됨.