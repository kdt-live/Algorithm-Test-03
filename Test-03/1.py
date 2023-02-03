'''
괄호 짝짓기
'''

# import sys
# sys.stdin = open('input.txt', 'r')

for _ in range(1,11):
    n = int(input())
    string = input()
    stack = []
    result = 0

    for i in string:
        if not stack:
            stack.append(i)
        else:
            if (stack[-1] == '(' and i == ')') or (stack[-1] == '[' and i == ']') or (stack[-1] == '{' and i == '}') or (stack[-1] =='<' and i == '>'):
                stack.pop()
            else:
                stack.append(i)
    
    if len(stack) == 0:
        result = 1
         

    print(f"#{_}", result)
