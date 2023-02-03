T = 10
for t in range(1, T+1):
    test_case = int(input())
    n_list = [*map(int, input().split())]
    while 0 not in n_list:
        for i in range(1,6):
            n_list[0] -= i
            if n_list[0] <= 0:
                n_list[0] = 0
            n_list.append(n_list.pop(0))
            if n_list[7] == 0:
                break
        if n_list[7] == 0:
            break
    print('#' + str(test_case), *n_list)