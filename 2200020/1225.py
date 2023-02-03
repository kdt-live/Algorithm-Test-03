T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    pw_list = list(map(int, input().split()))
    n = 1
    while n != 0:
        for x in range(1, 6):
            if pw_list[0] - x > 0:
                pw_list = pw_list[1:] + [pw_list[0]-x]
            else:
                pw_list = pw_list[1:] + [0]
                break
        n = pw_list[-1]
    print(f'#{tc}', *pw_list)