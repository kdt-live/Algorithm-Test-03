#6 1218 괄호 짝짓기
dic={
    '}':'{',
    ']':'[',
    ')':'(',
    '>':'<'
}

for i in range(10):
    t=int(input())
    arr=input()
    new_arr=[]
    print(f'#{i+1}',end=' ')
    for i in arr:
        if i in dic.values():
            new_arr.append(i)
            
        elif len(new_arr)>0 and new_arr[-1]==dic[i]:
            new_arr.pop()
            
        else:
            print(0)
            break
    else:
        if len(new_arr)>0:
            print(0)
        else:
            print(1)
