
for t in range(1, 11):
    n = int(input())
    numbers = list(map(int,input().split()))

    cnt = 1
    while True:
        if cnt > 5:
            cnt = 1
        t = numbers.pop(0) - cnt
        if t <= 0:
            numbers.append(0)
            break
        numbers.append(t)
        cnt += 1
    print(f'#{n}', *numbers)