a = ['(','[','{','<']
b = [')',']','}','>']
for test_case in range(1, 11):
    length = int(input())
    string = input()
    str_stack=[]

    for i in range(len(string)):
        if string[i] in a:
            str_stack.append(string[i])
        elif string[i] in b:
            if string[i] == b[0] and str_stack[-1] == a[0]:
                str_stack.pop()
            elif string[i] == b[1] and str_stack[-1] == a[1]:
                str_stack.pop()
            elif string[i] == b[2] and str_stack[-1] == a[2]:
                str_stack.pop()
            elif string[i] == b[3] and str_stack[-1] == a[3]:
                str_stack.pop()
            else:
                result=0
                break
    if len(str_stack) == 0:
        result=1

    print(f'#{test_case} {result}')