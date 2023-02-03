T = int(input())
 
for t in range(1,1+T):
 
    
    n,k = map(int,input().split())
 
    pe = list(map(int,input().split()))
    
    # 제출 안 한 사람 저장소
    notsub = []
 
    for i in range(1,n+1):
        if i not in pe:
            notsub.append(i)
 
    print('#{}'.format(t),*notsub)