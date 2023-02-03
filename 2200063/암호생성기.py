
for _ in range(10):
    T = int(input())
    N = list(map(int, input().split()))

    while N[-1] != 0:
        for n in range(1,6):
            if N[0] - n > 0:
                N.append(N.pop(0)-n)
            else:
                N.pop(0)
                N.append(0)
                break

    print(f'#{T}', *N, sep=' ')

        