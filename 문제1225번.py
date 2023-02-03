T = 10
for t in range(1, T + 1):
    input()
    answer = []
    input_list = list(map(int, input().strip().split(' ')))

    min_num = min(input_list)
    mok = min_num // 15

    if mok * 15 == min_num:
        mok -= 1

    input_list = list(map(lambda x: x - 15 * mok, input_list))

    idx = 0
    cnt = 0
    while True:
        idx %= 8
        cnt = cnt % 5 + 1
        input_list[idx] -= cnt
        
        if input_list[idx] <= 0:
            input_list[idx] = 0
            answer = input_list[idx + 1:] + input_list[:idx + 1]
            print(f'#{t} {" ".join(list(map(str, answer)))}')
            break

        idx += 1