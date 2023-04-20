#1225
# deque를 사용해서 pop(0)를 사용하지 않게함
from collections import deque

while True:
    t = int(input())
    nums = list(map(int, input().split()))
    nums = deque(nums)
    n = 0
    # nums[7] == 0이 아니라면 반복해
    while nums[7] != 0:
        # 반복 할 때마다 5가 되기 전까지 n을 1씩 증가
        n += 1
        if nums[0]-n > 0:
            nums.append(nums[0]-n)
        # 결과가 음수라면 nums[7]에 0을 넣어
        else:
            nums.append(0)
        # if와 상관없이 pop(0)를 지워줘    
        nums.popleft()

        if n == 5:
            n = 0

    print(f'#{t}', *nums)
    if t == 10:
        break
        