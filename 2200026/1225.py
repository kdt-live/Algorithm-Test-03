# 암호생성기 D3

for t in range(1, 10):
    N = int(input())
    # 8개의 숫자를 입력받는다
    number = list(map(int, input().split()))

    cnt = 1
    while True:
        # 맨 앞의 수에서 cnt를 뺏을때 (num)
        num = number[0] - cnt
        # num이 0보다 작거나 같다면
        if num <= 0:
            # num을 0으로 셋팅
            num = 0
        cnt += 1
        if cnt == 6:  # cnt가 6이되면 1로 셋팅
            cnt = 1
        number.pop(0)  # 첫번째 값 빼고
        number.append(num)  # 첫번째 값에서 cnt뺀 숫자를 append

        # 주어지는 각 수는 integer 범위를 넘지 않는다.
        if (number[0] < 10) and (number[1] < 10) and (number[2] < 10) and (number[3] < 10) and (number[4] < 10) and (number[5] < 10) and (number[6] < 10) and (number[7] < 10):
            break

    print(f'#{t}', end="")
    print(*number)

# while문으로 마지막값이 0이되면 종료했는데
# 알고보니 문제를 잘못이해함 무조건 1 ~ 5가 한 사이클
# 마지막 수가 0이라면 종료


# 값이 이상하게 나와서 다시 해야할 것 같다..
