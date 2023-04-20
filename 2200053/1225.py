# import sys
# sys.stdin = open('2200053/input.txt')

# 스택??
# from collections import deque
# queue = deque([10, 6, 12, 8, 9, 4, 1, 3])

# queue.popleft()
# print(queue)



# a = data[0] - 1
# data.pop(0)
# print(data)
# data.append(a)
# print(data) #[6, 12, 8, 9, 4, 1, 3, 9]


# a = data[0] - 2
# data.pop(0)
# print(data)
# data.append(a)
# print(data) #[12, 8, 9, 4, 1, 3, 9, 4]

# for i in range(1, 6):
#     a = data[0] - i
#     data.pop(0)
#     data.append(a)
# print(data) # 1 사이클 돌았음 [4, 1, 3, 9, 4, 9, 4, 4]

# while True:
#     for i in range(1, 6):
#         if data[-1] > 0:
#             a = data[0] - i
#             data.pop(0)
#             data.append(a)
        
#         else:
#             # data[-1]을 0으로 저장
#             data[-1] = 0
#             break
        
#         print(data)

