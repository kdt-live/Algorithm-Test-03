for n in range(1, 11):
    x = int(input())
    test_case = input()
    left = []
    right = [')',']','}','>']
    for i in test_case:
        if i not in right:
            left.append(i)
        else:
            if left == []:
                left.append(1)
                break
            else:
                a = left.pop()
                if i == ')':
                    if a == '(':
                        pass
                    else:
                        left.append(1)
                        break
                if i == ']':
                    if a == '[':
                        pass
                    else:
                        left.append(1)
                        break
                if i == '}':
                    if a == '{':
                        pass
                    else:
                        left.append(1)
                        break
                if i == '>':
                    if a == '<':
                        pass
                    else:
                        left.append(1)
                        break
                        
    if left == []:
        print(f'#{n}', 1)
    else:
        print(f'#{n}', 0)