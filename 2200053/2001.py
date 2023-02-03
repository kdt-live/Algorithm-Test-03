# ???

import sys
sys.stdin = open('2200053/input.txt')

T = int(input())
arr_list = []
for t in range(1, T+1):
    N, M = map(int, input().split())
    for _ in range(N):
        arr = list(map(int, input().split()))
        arr_list.append(arr)
        #print(arr)
    #print(arr_list)

    fly = []
    for i in range(M):
        for j in range(M):
            #print(arr_list[i][j])
            fly.append(arr_list[i][j])
    #print(sum(fly))

    print(f'#{t} {sum(fly)}')

    # 최대한 많은 파리를 죽이는 조건 세우기
        