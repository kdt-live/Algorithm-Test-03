t = int(input())
for i in range(1,t+1) :
    a,b = map(int,input().split())
    s = []
    for j in range(a) :
        c = list(map(int, input().split()))
        s.append(c)
    cnt_h = 0   # 가로 카운트
    cnt_v = 0 # 세로 카운트
    
    # 가로
    for x in range(len(s)) :
        h_cnt = []
        for y in s[x] :
            if y == 1 :
                h_cnt.append(y)
            elif y == 0 :
                if len(h_cnt) == b:
                    cnt_h +=1
                    h_cnt.clear()
                else : 
                    h_cnt.clear()
        if len(h_cnt) == b : 
            cnt_h +=1

    # 행렬 90도 회전
    new = [[0]*a for _ in range(a)]
    for e in range(a) :
        for r in range(a) :
            new[r][a-e-1] = s[e][r]  

    # 세로
    for f in range(len(new)) :
        v_cnt = []
        for d in new[f] :
            if d == 1 :
                v_cnt.append(d)
            elif d == 0 :
                if len(v_cnt) == b:
                    cnt_v +=1
                    v_cnt.clear()
                else : 
                    v_cnt.clear()
        if len(v_cnt) == b : 
            cnt_v +=1

    # 결과값 도출        
    result = cnt_h + cnt_v
    print(f'#{i} {result}')