import sys
sys.stdin = open("input4.txt", "r")

for i in range(1,int(input())+1):
    n,m = map(int,input().split())
    box = [list(map(int,input().split())) for _ in range(n)]
    word = 0
    for x in range(n):
        cnt = 0
        for y in range(n):
            if box[x][y] == 1:
                cnt += 1
            else:
                if cnt == m:
                    word += 1
                cnt = 0
        if cnt == m:
            word += 1
    for x in range(n):
        cnt = 0
        for y in range(n):
            if box[y][x] == 1:
                cnt += 1
            else:
                if cnt == m:
                    word += 1
                cnt = 0
        if cnt == m:
            word += 1

    print(f'#{i} {word}')
