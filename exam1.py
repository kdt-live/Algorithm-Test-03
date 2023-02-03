import sys
sys.stdin = open("input1.txt","r")
list1 = ['(','[','{','<']
list2 = [')',']','}','>']

result = []
for _ in range(10):
    a = 0
    b = 0
    c = 0
    d = 0
    T = int(input())
    string = input()
    for i in range(T):
        if string[i] == list1[0]:
            a += 1
        elif string[i] == list2[0]:
            a -= 1
        elif string[i] == list1[1]:
            b += 1
        elif string[i] == list2[1]:
            b -= 1
        elif string[i] == list1[2]:
            c += 1
        elif string[i] == list2[2]:
            c -= 1
        elif string[i] == list1[3]:
            d += 1
        elif string[i] == list2[3]:
            d -= 1
        if a<0 or b<0 or c<0 or d<0:
            result.append(0)
            break
    if a == 0 and b == 0 and c == 0 and d == 0:
        result.append(1)
    else:
        if a<0 or b<0 or c<0 or d<0:
            pass
        else:
            result.append(0)
for j in range(10):
    print("#%s %s"%((j+1),result[j]))