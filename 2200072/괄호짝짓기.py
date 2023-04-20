# solution1. - 성공/deque 이용
from collections import deque
for test_case in range(1,11):
    n = int(input())
    data = list(input())

    bracket = deque(data) 

    unit = {'(' : ')', '{':'}','[':']','<': '>'}
    stack = []
    while len(bracket) > 0 :
      if not stack: # 스택이 비워있으면
          # 닫힌 괄호가 먼저 나오면 0으로 바로 반환
          if bracket[0] in unit.values():
            stack = True
            break
          else:    
            stack.append(bracket.popleft())
      else: # 스택이 비워있지 않으면
          if unit[stack[-1]] == bracket[0]: # 닫힌 괄호가 짝이 맞으면
              bracket.popleft()
              stack.pop()
          
          # 닫힌 괄호가 짝이 안 맞으면
          elif bracket[0] in unit.values():
            stack = True
            break
          else: # 열린 괄호가 들어오면
              stack.append(bracket.popleft())

    if stack: # 빈 배열이 아니면
        print(f'#{test_case} 0')
    else: # 빈 배열이면
        print(f'#{test_case} 1')


# solution2 - 최종 코드/성공
for test_case in range(1,11):
    n = int(input())
    data = list(input())

    unit = {'(' : ')', '{':'}','[':']','<': '>'}
    stack = []
    for i in data:
        # 열린 괄호라면 스택에 추가
        if i in unit.keys():
            stack.append(i)
        # 닫힌 괄호라면
        else:
            # 빈 스택이 아니고 (& 닫힌 괄호라면)
            if stack:
                # 괄호의 짝이 맞으면 스택의 마지막 요소를 제거
                if unit[stack[-1]] == i:
                    stack.pop()
                # 괄호의 짝이 맞지 않으면 반복문을 종료
                else:
                    stack = True
                    break
            # 빈 스택 (& 닫힌 괄호라면)
            else:
                # 반복문 종료
                stack = True
                break

    if stack: # 빈 배열이 아니면
        print(f'#{test_case} 0')
    else: # 빈 배열이면
        print(f'#{test_case} 1')


