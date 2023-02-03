for t in range(1,11):
    N = int(input())
    word = list(input())
    a = word.count('(')
    b = word.count(')')
    c = word.count('[')
    d = word.count(']')
    e = word.count('<')
    f = word.count('>')
    g = word.count('{')
    h = word.count('}')
    if a == b and c == d and e == f and g == h:
        print(f'#{t} {1}')
    else:
        print(f'#{t} {0}')