#민석이의 과제 체크하기
test = int(input())
for T in range(1,test+1):
    n,task_n = map(int,input().split())
    ans_list = list(map(int,input().split()))
    n_list = [i for i in range(1,n+1)]
    for i in range(1,n+1):
        if i in ans_list:
            n_list.remove(i)
    print(f'#{T} ',end='')
    print(*n_list)
