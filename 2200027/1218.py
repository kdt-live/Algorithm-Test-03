#4일차 - 괄호 짝짓기
#10 + 1
for test_case in range(1, 10 + 1):
    length = int(input())
    text = input()
    cnt = {'(':0, '{':0, '[':0, '<':0}

    if len(text) % 2 != 0:
        print(f'#{test_case} 0')
    elif text.count('(') != text.count(')') or text.count('{') != text.count('}')\
        or text.count('[') != text.count(']'):
        print(f'#{test_case} 0')
    else:
        for _ in text:
            if -1 in cnt.values():
                print(f'#{test_case} 0')
                break
            elif _ in cnt.keys():
                cnt[_] += 1
            elif _ == ')':
                cnt['('] -= 1
            elif _ == ']':
                cnt['['] -= 1
            elif _ == '}':
                cnt['{'] -= 1
            else:
                cnt['<'] -= 1
        else:
            print(f'#{test_case} 1')
    
