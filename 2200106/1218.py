start = ['(', '[', '{', '<']
end = [')', ']', '}', '>']

for tc in range(1, 10+1):
    length = int(input())
    prob = input()
    res = []

    for i in range(len(prob)):
        if prob[i] in start:
            res.append(prob[i])
        if prob[i] in end:
            temp = res[-1]

            if end.index(prob[i]) == start.index(res[-1]):
                res.pop()
            else:
                print(f'#{tc} {0}')
                break
    else:
        if res:
            print(f'#{tc} {0}')
        else:
            print(f'#{tc} {1}')  
