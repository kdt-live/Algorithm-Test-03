# import sys
# sys.stdin = open("input (2).txt", "r")

# stack1 = []
# stack2 = []
# stack3 = []
# stack4 = []

# for i in range(1, 11):
#     T_length = int(input())
#     T = input()
#     for t in T:
#         if t == "(":
#             stack1.append("(")
#         elif t == ")":
#             if stack1 == []:
#                 print(f'#{i} 0')
#                 break
#             stack1.pop()
#         elif t == "[":
#             stack2.append("[")
#         elif t == "]":
#             if stack2 == []:
#                 print(f'#{i} 0')
#                 break
#             stack2.pop()
#         elif t == "{":
#             stack3.append("{")
#         elif t == "}":
#             if stack3 == []:
#                 print(f'#{i} 0')
#                 break
#             stack3.pop()
#         elif t == "<":
#             stack4.append("<")
#         elif t == ">":
#             if stack4 == []:
#                 print(f'#{i} 0')
#                 break
#             stack4.pop()
#     if len(stack1) == 0 and len(stack2) == 0 and len(stack3) == 0 and len(stack4) == 0:
#         print(f'#{i} 1')
#     else:
#         print(f'#{i} 0')

# 갯수만 똑같으면 되는 문제였냐..

import sys
sys.stdin = open("input (2).txt", "r")

from collections import Counter

for i in range(1, 11):
    T_length = int(input())
    T = input()
    # print(Counter(T))
    # print(Counter(T)["["])
    left = ["(", "[", "{", "<"]
    right = [")", "]", "}", ">"]
    for j in range(4):
        if Counter(T)[left[j]] == Counter(T)[right[j]]:
            result = 1
        else:
            result = 0
            break
    print(f'#{i} {result}')

    
