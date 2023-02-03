import sys
sys.stdin = open("input.txt", "r")

i_t = int(input())
for i_1 in range(i_t):
    i_n, i_k = map(int, input().split())
    lst_n = [list(map(int, input().split())) for i_2 in range(i_n)]
    i_cnt_x = 0
    i_cnt_y = 0
    for i_3 in range(i_n):
        i_x = 0
        for i_4 in range(i_n):
            if lst_n[i_3][i_4] == 1:
                i_x += 1
                if (i_4 == i_n - 1) * (i_x == i_k):
                    i_cnt_x += 1
            else:
                if i_x == i_k:
                    i_cnt_x += 1
                i_x = 0
    for i_5 in range(i_n):
        i_y = 0
        for i_6 in range(i_n):
            if lst_n[i_6][i_5] == 1:
                i_y += 1
                if (i_6 == i_n - 1) * (i_y == i_k):
                    i_cnt_y += 1
            else:
                if i_y == i_k:
                    i_cnt_y += 1
                i_y = 0            
    print(f'#{i_1 + 1} {i_cnt_x + i_cnt_y}')