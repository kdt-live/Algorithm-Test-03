for t in range (int(input())):
    n, k = map(int, input().split())
    assignment = list(map(int, input().split()))
    std = []

    for i in range (n):
        if i+1 not in assignment:
            std.append(i+1)

    std.sort()
    print(f'#{t+1}', *std)