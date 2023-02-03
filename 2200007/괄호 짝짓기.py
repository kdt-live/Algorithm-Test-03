T = 10

for t in range (1, 11) :
    N = int(input())
    str = input()
    stack = []
    val = 1

    for n in range (N) :
        if str[n] == '(' or str[n] == '{' or str[n] == '[' or str[n] == '<':
            stack.append(str[n])
        if str[n] == ')':
            if len(stack) > 0 and stack.pop() != '(':
                val = 0
                break
        if str[n] == '}':
            if len(stack) > 0 and stack.pop() != '{':
                val = 0
                break
        if str[n] == ']':
            if len(stack) > 0 and stack.pop() != '[':
                val = 0
                break
        if str[n] == '>':
            if len(stack) > 0 and stack.pop() != '<':
                val = 0
                break

    print(f"#{t} {val}")