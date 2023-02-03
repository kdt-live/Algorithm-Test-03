import sys

input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    n, k = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(n)]

    rotated_li = list(zip(*li))

    row_cnt, col_cnt = 0, 0

    for l, rl in zip(li, rotated_li):
        len_r, len_c = 0, 0
        for i in range(n):
            if l[i]:
                len_r += 1
            else:
                if len_r == k:
                    row_cnt += 1
                    len_r = 0
                else:
                    len_r = 0
            if rl[i]:
                len_c += 1
            else:
                if len_c == k:
                    col_cnt += 1
                    len_c = 0
                else:
                    len_c = 0
        if len_r == k:
            row_cnt += 1
        if len_c == k:
            col_cnt += 1
    print(f'#{t} {row_cnt+col_cnt}')