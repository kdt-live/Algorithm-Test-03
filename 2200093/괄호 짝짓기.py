for j in range(1, 11):
    N = int(input())
    case = list(input())
    check = []
    result = 1

    for i in range(N):
        if case[i] == ')':
            if '(' in check:
                check.pop(check.index('('))
            else:
                result = 0
                break
        
        elif case[i] == ']':
            if '[' in check:
                check.pop(check.index('['))
            else : 
                result = 0
                break        
        
        elif case[i] == '}':
            if "{" in check:
                check.pop(check.index('{'))
            else : 
                result = 0
                break

        elif case[i] == '>':
            if '<' in check:
                check.pop(check.index('<'))
            else : 
                result = 0
                break

        else:
            check.append(case[i])

    print(f'#{j} {result}')
        

    # while True:
    #     if('()' in case):
    #         case = case.replace('()', '')
    #     elif('{}' in case):
    #         case = case.replace('()', '')
    #     elif('[]' in case):
    #         case = case.replace('()', '')

    #     else:
    #         if (case == ''):
    #             print(f'#{i} 1')
    #             break

    #         else:
    #             result = 0
    #             break