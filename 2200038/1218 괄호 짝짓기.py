#1218 괄호 짝짓기
import sys
sys.stdin = open("1218.txt")

for test in range(1, 11):
    N=int(input())
    ls=list(input())
    sign=list()
    answer = 1

    for i in range(N):
        if ls[i] == ")":
            if "(" in sign:
                sign.pop(sign.index("("))
            else: 
                answer = 0
                break

        elif ls[i] == ">":
            if "<" in sign:
                sign.pop(sign.index("<"))
            else: 
                answer = 0
                break

        elif ls[i] == "}":
            if "{" in sign:
                sign.pop(sign.index("{"))
            else: 
                answer = 0
                break

        elif ls[i] == "]":
            if "[" in sign:
                sign.pop(sign.index("["))
            else: 
                answer = 0
                break

        else:
            sign.append(ls[i])

    print("#"+str(test),answer)