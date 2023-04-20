# 2001 파리 퇴치

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

for t in range(1,int(input())+1):
    n, m = map(int,input().split())
    li = [list(map(int,input().split())) for _ in range(n)]
    
    cnt_li = []
    for i in range(n-m+1):
        for j in range(n-m+1):
            cnt = 0
            for ii in range(m):
                for jj in range(m):
                    cnt += li[i+ii][j+jj]
            cnt_li.append(cnt)

    print(f'#{t}', max(cnt_li))