
for i in range(10):
    a = int(input())
    b = input()
    stack = []
    for j in b:
        if j in'{([<':
            stack.append(j)
        elif j == '}':
            if stack[-1] =='{':
                stack.pop()
            else:
                print(f'#{i+1} 0')
                break
        elif j == ']':
            if stack[-1] =='[':
                stack.pop()
            else:
                print(f'#{i+1} 0')
                break
        elif j == '>':
            if stack[-1] =='<':
                stack.pop()
            else:
                print(f'#{i+1} 0')
                break
        elif j == ')':
            if stack[-1] =='(':
                stack.pop()
            else:
                print(f'#{i+1} 0')
                break
    else:
        if stack:
            print(f'#{i+1} 0')
        else:
            print(f'#{i+1} 1')
