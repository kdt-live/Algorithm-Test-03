T = int(input())
for i in range(T):
    a, b = map(int,input().split())
    c = []
    sum = 0
    arr = [[0 for _ in range(a) ] for _ in range(a)]
    for j in range(a):
        d = list(map(int,input().split()))
        for k in range(a):
            arr[j][k] = d[k]
    for l in range(a-b+1):
        for m in range(a-b+1):
            for n in range(b):
                for o in range(b):
                    sum += arr[l+n][m+o]
            c.append(sum)
            sum = 0
    c = sorted(c,reverse=True)
    print(f"#{i+1} {c[0]}")


