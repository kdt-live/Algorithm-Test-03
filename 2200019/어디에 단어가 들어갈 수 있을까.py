T = int(input())

for i in range(1,T+1):
    a, b = map(int,input().split())
    a_list = []
    for _ in range(a):
        a_list.append(list(map(int,input().split())))

    # 가로줄
    satisfied = 0
    
    for j in range(a):
        cnt = 0
        for k in a_list[j]:
            if k == 1:
                cnt +=1
            else:
                cnt = 0
            if cnt == b:
                satisfied += 1
            elif cnt == b+1:
                satisfied -= 1
    
    # 세로줄

    for p in range(a):
        cnt = 0
        for q in range(a):
            if a_list[q][p] ==1:
                cnt += 1
            else:
                cnt = 0
            if cnt == b:
                satisfied += 1
            elif cnt == b+1:
                satisfied -= 1
                
    print(f'#{i} {satisfied}')
    