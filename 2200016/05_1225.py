# 1225 암호생성기
for i in range(10):
    T = int(input())
    n = list(map(int,input().split()))
    while True:
        for i in range(1,6):    
            a = n.pop(0)
            b = a-i
            if b <= 0:
                b = 0
                n.append(b)
                break
                print(n)
            else:
                n.append(b)
        if n[7] == 0:
            break
    print(f'#{T}',*n)