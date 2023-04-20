# 괄호 짝짓기
op = ['(', '[', '{', '<']
cl = [')', ']', '}', '>']
for t in range(1, 11):
    n = int(input())
    string = input()
    opcnt = 0
    clcnt = 0
    bras = []
    collect = 1

    for bra in string:
        if bra in op:
            opcnt += 1
        else:
            clcnt += 1

    if opcnt != clcnt:
        collect = 0

    for bra in string:
        if bra in op:
            bras.append(bra)
        else:
            if op[cl.index(bra)] in bras:
                bras.remove(op[cl.index(bra)])
            else:
                collect = 0

    print(f'#{t} {collect}')