for t in range (10):
    length = int(input())
    bracket = input()
    stack = []
    check = False

    for br in bracket:
        if br == '(' or br == '{' or br =='[' or br == '<':
            stack.append(br)
        
        else:
            if br == ')' and '(' in stack:
                stack.remove('(')
                check = True
            elif br == '}' and '{' in stack:
                stack.remove('{')
                check = True
            elif br == ']' and '[' in stack:
                stack.remove('[')
                check = True
            elif br == '>' and '<' in stack:
                stack.remove('<')
                check = True
            
            else:
                check = False
                break
    
    if stack:
        check = False
    
    if check:
        print(f'#{t+1} 1')

    else:
        print(f'#{t+1} 0')