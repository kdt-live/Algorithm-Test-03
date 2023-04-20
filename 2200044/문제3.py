T = int(input())
for i in range(T):
    b, c = map(int,input().split())
    a1 = set(range(1,b+1))
    a2 = set(list(map(int,input().split())))
    print(f"#{i+1}",end=' ')
    for elem in (a1 - a2):
        print(elem,end = ' ')
    print()