# 파리 퇴치
test = int(input())
for T in range(1,test+1):
    n,m = map(int,input().split())
    n_list = [list(map(int,input().split())) for _ in range(n)]
    m_sum = 0
    m_list=[]
    # mxm 배열 만들고 세로덧셈
    for k in range(n-m+1):
        for fly in range(n-m+1):
            m_sum = 0
            for i in range(fly,m+fly):
                for j in range(k,m+k):
                    m_sum += n_list[i][j]
            m_list.append(m_sum)
    print(f'#{T} {max(m_list)}')