'''
암호생성기
'''

# import sys
# sys.stdin=open('input2.txt', 'r')

for t in range(1, 11):
    s = input()
    queue = list(map(int, input().split()))
    i = 1
    while 1:
        a = queue.pop(0) - i
        
        if a < 0:
            a = 0
        queue.append(a)
        
        if a <= 0:
            break
        i += 1
        
        if i > 5:
            i = 1
    print(f'#{t}', *queue)
    