# 괄호 짝짓기

for i in range(1, 11):
    nums = int(input())
    brackets = input()
    stack = []
    result = "1"
    for j in brackets:        
        if j in "({[<":
            stack.append(j)
        elif j == ")":
            if not stack or stack[-1] != "(":
                result = "NO"
                break
            stack.pop()
        elif j == "}":
            if not stack or stack[-1] != "{":
                result = "NO"
                break
            stack.pop()
        elif j == "]":
            if not stack or stack[-1] != "[":
                result = "NO"
                break
            stack.pop()
        elif j == ">":
            if not stack or stack[-1] != "<":
                result = "NO"
                break
            stack.pop()
    if stack:
        result = "0"
    print(f"#{i} {result}")
