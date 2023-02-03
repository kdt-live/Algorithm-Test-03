#5431
T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    not_input = []

    for num in range(1, N + 1):
        # 숙제를 내지 않은 번호를 찾아 append한다
        if num not in nums:
            not_input.append(num)
    
    print(f"#{t}", *sorted(not_input))
