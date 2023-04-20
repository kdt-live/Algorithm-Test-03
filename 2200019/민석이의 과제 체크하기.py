T = int(input())

for i in range(1,T+1):
    a, b = map(int,input().split())
    b_list = list(map(int,input().split()))
    f_list = []
    for j in range(1,a+1):
        if j not in b_list:
            f_list.append(j)
    print(f'#{i}', *f_list)
    