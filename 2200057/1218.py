import sys

input = sys.stdin.readline

for i in range(1, 11):
    n = int(input())
    string = input().strip()

    stack = []

    for s in string:
        if s in '({[<':
            stack.append(s)
        elif s == ')' and stack[-1] == '(':
            stack.pop()
        elif s == '}' and stack[-1] == '{':
            stack.pop()
        elif s == ']' and stack[-1] == '[':
            stack.pop()
        elif s == '>' and stack[-1] == '<':
            stack.pop()
        else:
            print(f'#{i} 0')
            break
    else:
        if stack:
            print(f'#{i} 0')
        else:
            print(f'#{i} 1')