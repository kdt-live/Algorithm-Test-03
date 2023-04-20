# import sys
# sys.stdin = open("input.txt", "r")

# # T = int(input())
# # nums = list(map(int, input().split()))

# # cnt = 0
# # while True:
# #     cnt += 1
# #     if nums[0] - cnt <= 0:
# #         print(nums)
# #         nums.append(0)
# #         nums.pop()             ##### pop에 0 빼먹은걸 두시간 가까이 못 찾은게 말이되냐
# #         print(nums)
# #         break
# #     nums.append(nums[0] - cnt)
# #     nums.pop(0)
# #     if cnt == 5:
# #         cnt = 0

import sys
sys.stdin = open("input.txt", "r")

while True:
    try:
        T = int(input())
        nums = list(map(int, input().split()))

        cnt = 1
        while True:
            if cnt > 5:
                cnt = 1
            if nums[0] - cnt <= 0:
                nums.append(0)
                nums.pop(0)
                print(f'#{T}', *nums)
                break
            if cnt <= 5:
                nums.append(nums[0] - cnt)
                nums.pop(0)

            cnt += 1
    except:
        break
