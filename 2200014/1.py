#1 5431 민석이의 과제 체크하기


t=int(input())

for i in range(1,t+1):
    n,k=map(int,input().split())
    arr=[]
    arr.append(list(map(int,input().split())))
    print(f'#{i}',end=' ')
    for i in range(1,n+1):
        if i not in arr[0]:
            
            print(i,end=' ')
    print()