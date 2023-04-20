c = ['[','{','<','(']
d= [']','}','>',')']
for j in range(1,11):
    e=0
    a= int(input())
    b= list(map(str,input()))
    for i in b:
        if i in c[0]:
            e += 1
        elif i in d[0]:
            e -= 1
        elif i in c[1]:
            e += 20
        elif i in d[1]:
            e -= 20
        elif i in c[2]:
            e += 300
        elif i in d[2]:
            e -= 300
        elif i in c[3]:
            e += 4000
        elif i in d[3]:
            e -= 4000

    if e == 0:
        print(f'#{j} 1')
        
    else:
        print(f'#{j} 0')
        