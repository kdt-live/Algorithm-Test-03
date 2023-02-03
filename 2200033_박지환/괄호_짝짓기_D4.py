
for k in range(1, 11):
    T = int(input())
    strs = input()

    box = []
    for i in range(len(strs)):
        try:
            if strs[i] in ['(', '[', '{', '<']: # 여는 괄호의 경우 넣어주고
                box.append(strs[i])

            elif strs[i] == ')': # 닫는 괄호의 경우 빼준다
                if box.pop() != '(':
                    break
            elif strs[i] == ']':
                if box.pop() != '[':
                    break
            elif strs[i] == '}': 
                if box.pop() != '{':
                    break
            elif strs[i] == '>':
                if box.pop() != '<':
                    break
            
        except: # 여는 괄호 없이 닫는 괄호만 있었을 경우, pop() 과정에서 에러가 생긴다.
            box.append('end') # 이때 'end'라는 문자를 넣어서 적어도 box가 비어있지 않은 상황으로 만든다.
            break

    if box:
        print(f'#{k} 0')
    else:
        print(f'#{k} 1')                    