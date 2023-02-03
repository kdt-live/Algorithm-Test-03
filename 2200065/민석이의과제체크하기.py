for i in range(1,int(input())+1):
    a, b = map(int,input().split())
    lst = set([j for j in range(1,a+1)])
    lst2 = set(list(map(int,input().split())))
    print(f'#{i}',*lst-lst2)