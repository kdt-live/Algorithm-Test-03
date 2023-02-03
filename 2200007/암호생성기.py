T = 10

for t in range (1, 11) :
    N = int(input())
    num = list(map(int,input().split()))
    i = 1

    while True:
        a = num.pop(0) - i
        if a < 0 :
            a = 0
        num.append(a)
        if a <= 0 : 
            break
        i += 1
        if i > 5 : 
            i = 1
            
    print(f"#{t}", *num)