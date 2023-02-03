import sys
input = sys.stdin.readline
# word_list = [['{', '[', '(','<'], ['}', ']', ')', '>']]
# left = word_list[0]
# right = word_list[1]
# stack = []
    

# tc = int(input())
# for t in range(1, tc+1):
#     number = int(input())
#     string = list(map(str, input().rstrip()))
#     for i in range(number):
#         if string[i] in left:
#             stack.append(string[i])
#         if string[i] in right:
#             if right.index(string[i]) == left.index(stack[-1]):
#                 stack.pop()
#             else:
#                 break
#     answer = 0
#     if len(stack) == 0:
#         answer = 1
#     print(f"#{t} {answer}")

from collections import deque
word_list = {'[':']', '{':'}', '(':')', '<':'>'}
T = int(input())
for t in range(1, T+1):
    answer = 1
    length = int(input())
    stack = deque()
    string = input()
    for i in string:
        if i in word_list.keys():
            stack.append(i)
        else :
            if word_list[stack[-1]] == i :
                stack.pop()
            else:
                answer = 0
                break

    print(f'#{t} {answer}')


