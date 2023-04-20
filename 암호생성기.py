n = 10
for k in range(1,n+1) :
    a = int(input())
    s = list(map(int,input().split()))
    result = ""
    while s[-1] > 0 :
        for i in range(1,6) :
            if s[-1] <=0:
                break
            else:
                s[0] -=i
                first = s[0]
                s.pop(0)
                s.append(first)
    if s[-1] <= 0 :
        s[-1] = 0
    for j in s :
        result += (str(j) + " ")
    print(f'#{a} {result}')