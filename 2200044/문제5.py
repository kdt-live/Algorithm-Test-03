from math import floor
T = int(input())
score = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D']
c= {}
sum = 0
for i in range(T):
    a, b = map(int,input().split())
    for j in range(a):
        d = list(map(int,input().split()))
        c[j+1] = (d[0]*35+d[1]*45+d[2]*20)/100
    d = sorted(c.values(),reverse=True)
    for k in range(len(d)):
        if d[k] == c[b]:
            print(f"#{i+1} {score[floor(k/(a/10))]}")