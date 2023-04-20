#3 1983 조교의 성적 매기기

dic={}
t=int(input())
for t in range(t):
    n,k=map(int,input().split())
    grade_arr=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    arr=[]
    for i in range(1,n+1):
        midterm,final,report=map(int,input().split())
        grades=midterm*0.35+final*0.45+report*0.2
        arr.append([i,grades])
        dic[i]=grades
    arr.sort(key=lambda x:x[1],reverse=True)
    place=0 #위치 찾기
    cnt=0
    for i in arr:
        if i[0]==k:
            place=cnt
        cnt+=1
    
    
    
    print(f'#{t+1}',grade_arr[int(place/(n//10))])