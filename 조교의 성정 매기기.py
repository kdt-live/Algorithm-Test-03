T = int(input())
for i in range(1,T+1):
    a, b = map(int,input().split())
    all = {}
    for j in range(a) :
        score = list(map(int,input().split()))
        score_cnt = (score[0]*0.35) + (score[1]*0.45) + (score[2]*0.2)
        all[j+1] = score_cnt
    all1= sorted(all.items(), key = lambda x:x[1], reverse = True)
    result = 0
    for x in range(len(all1)) :
        if all1[x][0] == b:
            result = x+1
    if result <= a*0.1  :
        print(f'#{i} A+')
    if result > a*0.1 and result <= a*0.2 :
        print(f'#{i} A0')
    if result > a*0.2 and result <= a*0.3 :
        print(f'#{i} A-')
    if result > a*0.3 and result <= a*0.4 :
        print(f'#{i} B+')
    if result > a*0.4 and result <= a*0.5 :
        print(f'#{i} B0')
    if result > a*0.5 and result <= a*0.6 :
        print(f'#{i} B-')
    if result > a*0.6 and result <= a*0.7 :
        print(f'#{i} C+')
    if result > a*0.7 and result <= a*0.8 :
        print(f'#{i} C0')
    if result > a*0.8 and result <= a*0.9 :
        print(f'#{i} C-')
    if result > a*0.9 and result <= a*1 :
        print(f'#{i} D0')