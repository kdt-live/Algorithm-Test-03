T = 10

for i in range(1,T+1):
    test_case = int(input())
    queue = list(map(int,input().split()))

    k = 1
    while True:
        if k > 5:
            k = 1
        i = queue.pop(0) - k

        if i <= 0:
            queue.append(0)
            break

        queue.append(i)
        k += 1

    print("#{} {} {} {} {} {} {} {} {}".format(test_case, *queue))