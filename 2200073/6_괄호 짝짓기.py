import sys
sys.stdin = open('input_6.txt', 'r')

for t in range(10):
    n = int(input())
    d = input()
    stack = []
    f = 1
    for i in d:
        if i == '(' or i == '[' or i == '{' or i == '<':
            stack.append(i)
        elif i == ')':
            if stack.pop() != '(':
                f = 0
                break
        elif i == ']':
            if stack.pop() != '[':
                f = 0
                break
        elif i == '}':
            if stack.pop() != '{':
                f = 0
                break
        elif i == '>':
            if stack.pop() != '<':
                f = 0
                break
    else:    
        if stack:
            f = 0
        else:
            f = 1
    print(f'#{t+1} {f}')
