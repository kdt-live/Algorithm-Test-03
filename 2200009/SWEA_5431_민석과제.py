i_t = int(input())
for i_1 in range(i_t):
    i_n, i_k = map(int, input().split())
    set_k = set(map(int, input().split()))
    lst_bad = []
    for i_2 in range(1, i_n + 1):
        if i_2 not in set_k:
            lst_bad.append(i_2)
    print(f'#{i_1 + 1}',end= ' ')
    print(*lst_bad)