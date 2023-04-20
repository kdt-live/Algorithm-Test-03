T = int(input())

for i in range(1,T+1):
    N, M = map(int,input().split())
    N_list = []
    for _ in range(N):
        N_list.append(list(map(int,input().split())))
    
    # 파리채 휘두른다
    
    m_cnt = 0
    # 세로축
    for p in range(N-M+1):                          # 5 2 경우 세로축을 4번 횡단한다.
        
    # 가로축
        for q in range(N-M+1):                      # 5 2 경우 가로축을 4번 횡단한다.
            cnt = 0
        
            for p_ in range(M):                      # 세로축
                for q_ in range(M):                  # 가로축
                    cnt += N_list[p+p_][q+q_]
                    
            if cnt > m_cnt :
                m_cnt = cnt
                
    print(f'#{i}',m_cnt)
            
            
            