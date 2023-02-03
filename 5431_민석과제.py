T = int(input())

for t in range(1, T+1) :
    n, k = map(int, input().split()) # n : 수강생 수 , k : 제출 수
    li = list(map(int, input().split()))

    tot_li = list(range(1, n+1))
    # print(tot_li-li)
    for i in li :
        tot_li.remove(i)
    print(f'#{t}', end=' ')
    print(*tot_li)