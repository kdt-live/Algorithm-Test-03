tc = int(input())
for j in range(tc):
    a,b = map(int,input().split())
    l = list(map(int,input().split()))
    l2 = [x for x in range(1,a+1)]
    for i in l:
        l2[i-1] = 0
    print('#',end='')
    print(j+1,end=' ')
    for k in l2:
        if k != 0:
            print(k,end=' ')
    print()