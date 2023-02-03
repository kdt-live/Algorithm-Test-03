import sys
sys.stdin = open("input2.txt", "r")

a = ['{','[','(','<']
b = ['}',']',')','>']

for i in range(1,11):
    input()
    n = input()
    cnt = 0
    for m in n:
        if m in a:
            cnt += (a.index(m)+1)
        if m in b:
            cnt -= (b.index(m)+1)
            if cnt < 0:
                print(f'#{i} 0')
                break
    else:
        if cnt == 0:
            print(f'#{i} 1')
        else:
            print(f'#{i} 0')
