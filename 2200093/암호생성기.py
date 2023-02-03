for _ in range(10):
    T = int(input())
    password = list(map(int, input().split()))

    i = 1
    while True:

        if i > 5:
            i = 1
        new = password.pop(0) - i
        
        if new <= 0:
            password.append(0)
            break
        password.append(new)
        i += 1
    
    print(f'#{T}', *password)