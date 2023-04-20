for t in range (10):
    N = int(input())
    code = list(map(int, input().split()))
    check = 0

    while code:
        for i in range (1, 6):
            n = code.pop(0)

            if n-i <= 0:
                code.append(0)
                check = 1
                break
            
            code.append(n-i)
        
        if check:
            break

    print(f'#{t+1}', *code)