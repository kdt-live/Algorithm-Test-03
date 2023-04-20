for i in range(1,11):
    a = int(input())
    b = list(map(int,input().split()))
    c=1
    while True:
        if b[7] > 0:
            b.append(b.pop(0)-c)
            c+=1
            if c == 6:
                c = 1

        elif b[7]<=0:
            b[7] = 0 
            break

    print(f'#{i}',*b)
