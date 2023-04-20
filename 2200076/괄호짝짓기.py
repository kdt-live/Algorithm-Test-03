for t in range(10):
    n = int(input())
    string = input()
    stack = []
    for i in range(n):
        if string[i] in ['(', '[', '{', '<']:
            stack.append(string[i])
        else:
            # stack이 비어있는 경우와 그렇지 않은 경우 구분
            if stack:
                # 괄호의 짝이 맞는지 확인
                if string[i] == ')' and stack[-1] == '(':
                    stack.pop()
                elif string[i] == ']' and stack[-1] == '[':
                    stack.pop()
                elif string[i] == '}' and stack[-1] == '{':
                    stack.pop()
                elif string[i] == '>' and stack[-1] == '<':
                    stack.pop()
                else:
                    print(f'#{t+1} 0')
                    break
            else:
                print(f'#{t+1} 0')
                break
    else:
        print(f'#{t+1} 0' if stack else f'#{t+1} 1')