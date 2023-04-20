T = 10

for t in range(1, T+1):
    count = int(input())
    q = list(map(int, input().split()))
    
    i = 1
    while True:
        if i > 5:
            i = 1
        t = q.pop(0) - i
        if t <= 0:
            q.append(0)
            break
        q.append(t)
        i += 1
    print("#{} {} {} {} {} {} {} {} {}".format(count, *q))