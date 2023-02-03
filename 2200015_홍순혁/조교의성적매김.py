t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    c=[0]*n
    d={}
    for j in range(n):
        a = list(map(int,input().split()))
        c[j] = (a[0]*0.35+a[1]*0.45+a[2]*0.2)/3
        
print(c)