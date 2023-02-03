
for tc in range(10):
    N = int(input())
    arr = list(map(str, input()))
    lst = list()


    left = ['(', '{', '[', '<']
    right = [')', '}', ']', '>']
    for i in range(N):
        if arr[i] in left:
            lst.append(arr[i])
        if arr[i] in right:
           
            if right.index(arr[i]) == left.index(lst[-1]):
               
                lst.pop()   
            else:
                break
                
    result = 0
    if len(lst) == 0:
        result = 1
    
    print("#{} {}".format(tc + 1, result))

