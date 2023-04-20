#4 1979 어디에 단어가 들어갈 수 있을까\

t=int(input())
for t in range(t):
    n,k=map(int,input().split())

    arr=[list(map(int,input().split()))for i in range(n)]
    cnt=0 #연속 몇칸인지 카운트
    cnt_k=0 # k칸이 몇개인지
    for i in arr:
        cnt=0 #각 배열마다 초기화
        for j in i:
            if j==1:
                cnt+=1
            else:
                cnt=0
            if cnt==k:
                cnt_k+=1
            elif cnt==k+1:
                cnt_k-=1

    for i in range(n):
        cnt=0
        for j in range(n):
            if arr[j][i]==1:
                cnt+=1
            else:
                cnt=0
            if cnt==k:
                cnt_k+=1
            elif cnt==k+1:
                cnt_k-=1
    print(f'#{t+1}',cnt_k)    