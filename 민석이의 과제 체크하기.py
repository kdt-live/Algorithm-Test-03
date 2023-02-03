T= int(input())
for i in range(1,T+1) :
    a,b = map(int,input().split())
    s = list(map(int,input().split()))
    stu = []
    result = ""
    for j in range(1,a+1) :
        stu.append(j)
    for x in s :
        stu.remove(x)
    for y in stu:
        result += str(y) + " "
    print(f"#{i} {result}")