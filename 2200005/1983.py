grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
tc = int(input())
for i in range(tc):
    x,y = map(int,input().split())
    l = []
    for j in range(x):
        a,b,c= map(int,input().split())
        score = (a*35 + b*45 + c*20) 
        l.append(((j+1),score))
    l = sorted(l,key=lambda x: -x[1])
    
    for j in l:
        if j[0] == y:
            v = l.index(j)//(x//10)
            print(f'#{i+1} {grade[v]}') 
