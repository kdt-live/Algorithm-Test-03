# 괄호 짝짓기

for i in range(1, 11):
    T = int(input())
    l = ['(', '[', '{', '<']
    r = [')', ']', '}', '>']
    p = []

    case = input()
    for j in range(T):
        if case[j] in l:
            p.append(case[j])
        if case[j] in r:
            if r.index(case[j]) == l.index(p[-1]):
                p.pop()
            else:
                break
        
    if len(p) == 0:
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')




# 실패
# for i in range(1, 11):
#     T = int(input())
#     case = input()
#     while ('()' or '[]' or '{}' or '<>') in case:
#         case = case.replace('()', '')
#         case = case.replace('[]', '')
#         case = case.replace('{}', '')
#         case = case.replace('<>', '')
            
#     if len(case) == 0:
#         print(f'#{i} 1')
#     else:
#         print(f'#{i} 0')