for _ in range(10):
    n = int(input())
    a = list(map(int, input().split()))

    while True:
        for i in range(1, 6):
            if (a[0]-i) <= 0:
                a.pop(0)
                a.append(0)
                break
            else:
                a.append(a.pop(0)-i)
        if a[7] == 0:
            break

    print(f'#{n}', *a)