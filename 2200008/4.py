# 어디에 단어가 들어갈 수 있을까
for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    puz = [list(map(int, input().split()))+[0] for _ in range(n)]
    puz.append([0]*(n+1))
    wrd = 0
    for i in range(n+1):
        hcnt = 0
        vcnt = 0
        for j in range(n+1):
            if puz[i][j] == 1:
                hcnt += 1
            else:
                if hcnt == k:
                    wrd += 1
                hcnt = 0

            if puz[j][i] == 1:
                vcnt += 1
            else:
                if vcnt == k:
                    wrd += 1
                vcnt = 0

    print(f'#{t} {wrd}')