for t in range(1, 11):
    n = int(input())
    lst = list(map(str,input()))
    
    a1 = lst.count('(') # 각 문자들의 개수를 카운트 해준다
    a2 = lst.count(')')
    b1 = lst.count('[')
    b2 = lst.count(']')
    c1 = lst.count('{')
    c2 = lst.count('}')
    d1 = lst.count('<')
    d2 = lst.count('>')
    if a1 == a2 and b1 == b2 and c1 == c2 and d1 == d2: # 각 문자들의 개수가 모두 같다 아니다로 유효 판단 
        result = 1 # 같다면 1
    else:
        result = 0 # 아니면 0
    print(f'#{t} {result}')