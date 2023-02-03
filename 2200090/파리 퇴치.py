for t in range(1, int(input())+1):
    m, n = map(int, input().split())
    pali = []
    mm = []

    for _ in range(m):
        pali.append(list(map(int, input().split())))
    for i in range(m-n+1): # m = 5로 입력 시 범위를 벗어나므로 0 1 2 3 까지만
        for j in range(m-n+1):
            cnt = 0 # 합 저장 및 초기화 변수
            for k in range(n):
                for l in range(n):
                    cnt += pali[i+k][j+l]
            mm.append(cnt)
    print(f'#{t} {max(mm)}')