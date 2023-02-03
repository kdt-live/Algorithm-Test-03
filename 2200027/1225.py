#7일차 - 암호생성기
from collections import deque

for case in range(1,11):
    test = int(input())
    nums = deque(list(map(int, input().split())))

    flag = True
    while (flag):
        for minus in range(1,6):
            if nums[0] - minus <= 0:
                nums.append(0)
                nums.popleft()
                flag = False
                break
            else:
                nums.append(nums[0] - minus)
                nums.popleft()
    print(f'#{case}', *nums)

