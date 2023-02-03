for j in range(10):
    stack = []
    k = int(input())
    l = input()
    for i in range(k):
        if l[i] == '(':
            stack.append('(')
        if l[i] == '[':
            stack.append('[')
        if l[i] == '{':
            stack.append('{')
        if l[i] == '<':
            stack.append('<')
        if i > 0:
            if l[i] == '>' and stack[len(stack)-1] == '<':
                stack.pop()
            if l[i] == ']' and stack[len(stack)-1] == '[':
                stack.pop()
            if l[i] == '}' and stack[len(stack)-1] == '{':
                stack.pop()
            if l[i] == ')' and stack[len(stack)-1] == '(':
                stack.pop()
        else:
            break
    if stack == []:
        print(f"#{j+1} 1")
    else:
        print(f"#{j+1} 0")