import sys
sys.stdin = open("input.txt", "r")
# tmp = ['(', ')', '[', ']', '{', '}', '<','>']
for t in range(1, 11):
    T = int(input())
    string = input()
    tmp = {}
    for i in string:
        if i not in tmp:
            tmp[i] =  1
        else:
            tmp[i] +=1
    tmp_set = set(tmp.values())
    if len(tmp_set)/4 == 1:
        print(f'#{t} {1}')
    elif len(tmp_set) <= 3:
        print(f'#{t} {1}')
    else:
        print(f'#{t} {0}')
    
    # print((tmp.values()))
    # # for i in tmp:
    # #     tmps.append(string.count(i))
    # # tmps_s = set(tmps)
    # # print(tmps_s)



