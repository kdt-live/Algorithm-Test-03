import sys
sys.stdin = open("input5.txt", "r")

for t in range(10):
    n = input()
    lst = list(map(int,input().split()))
    while lst[-1] > 0:
        for i in range(1,6):
            if lst[0] - i <= 0:
                lst.pop(0)
                lst.append(0)
                break
            else:
                lst.append(lst.pop(0)-i)
    print(f'#{n}',*lst)