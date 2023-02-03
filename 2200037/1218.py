# 괄호 짝짓기
for T in range(1,11):
    n = int(input())
    in_s = input()
    stack = []
    answer = 1
    chk_list = ['(','{','[','<']
    for i in in_s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if '(' in stack:
                stack.remove('(')
            else:
                answer = 0

        if i == '{':
            stack.append(i)
        elif i == '}':
            if '{' in stack:
                stack.remove('{')
            else:
                answer = 0

        if i == '[':
            stack.append(i)
        elif i == ']':
            if '[' in stack:
                stack.remove('[')
            else:
                answer = 0

        if i == '<':
            stack.append(i)
        elif i == '>':
            if '<' in stack:
                stack.remove('<')
            else:
                answer = 0

    if answer == 1 and stack == []:
        print(f'#{T} {answer}')
    else:
        print(f'#{T} {0}')