for t in range(1, 11):
    n = int(input())
    pawd = list(map(int, input().split()))
    c = 1
    
    while True:
        if c > 5:
            c = 1
        cycle = pawd.pop(0) - c
        
        if cycle <= 0:
            pawd.append(0)
            break
        pawd.append(cycle)
        c += 1
    print(f'#{t}', *pawd)