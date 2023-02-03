for i_1 in range(10):
    i_t = int(input())
    lst_n = list(map(int, input().split()))
    i_cycle = 0
    i_cnt = 0
    while lst_n[7] > 0:
        i_cnt += 1
        lst_n[0] -= i_cnt
        lst_n.append(lst_n[0])
        lst_n.pop(0)
        if i_cnt == 5:
            i_cnt = 0
    lst_n[7] = 0
    print(f'#{i_t}', end= ' ')
    print(*lst_n)