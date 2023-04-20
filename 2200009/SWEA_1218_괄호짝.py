for i_1 in range(10):
    i_n = int(input())
    s_n = input()
    i_round = 0
    i_square = 0
    i_curly = 0
    i_angle = 0
    for s_1 in s_n:
        if s_1 == '(':
            i_round += 1
        elif s_1 == ')':
            i_round -= 1
        elif s_1 == '[':
            i_square += 1
        elif s_1 == ']':
            i_square -= 1
        elif s_1 == '{':
            i_curly += 1
        elif s_1 == '}':
            i_curly -= 1
        elif s_1 == '<':
            i_angle += 1
        elif s_1 == '>':
            i_angle -= 1
        if (i_round < 0) + (i_square < 0) + (i_curly < 0) + (i_angle < 0): 
            print(f'#{i_1 + 1} 0')
            break
    else:
        print(f'#{i_1 + 1} 1')                                                           