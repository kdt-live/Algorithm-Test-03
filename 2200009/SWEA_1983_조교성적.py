lst_test = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
i_t = int(input())
for i_1 in range(i_t):
    i_n, i_k = map(int, input().split())
    dict_score = {}
    for i_2 in range(i_n):
        i_sc_1, i_sc_2, i_sc_3 = map(int, input().split())
        i_sc_total = 0.35 * i_sc_1 + 0.45 * i_sc_2 + 0.20 * i_sc_3
        dict_score[i_2 + 1] = i_sc_total
    lst_score = sorted(dict_score.items(), key = lambda x: -x[1])
    for i_3 in range(i_n):
        if lst_score[i_3][0] == i_k:
            print(f'#{i_1 + 1} {lst_test[int(i_3//(i_n/10))]}')