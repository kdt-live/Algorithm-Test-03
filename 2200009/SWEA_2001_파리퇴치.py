i_t = int(input())
for i_1 in range(i_t):
    i_n, i_m = map(int, input().split())
    lst_fly = [list(map(int, input().split())) for i_2 in range(i_n)]
    i_maxcatch = 0
    for i_3 in range(i_n - i_m + 1):
        for i_4 in range(i_n - i_m + 1):
            i_catch = 0
            for i_5 in range(i_m):  
                for i_6 in range(i_m):
                    i_catch += lst_fly[i_3 + i_5][i_4 + i_6]
            if i_catch > i_maxcatch:
                i_maxcatch = i_catch
    print(f'#{i_1 + 1} {i_maxcatch}')