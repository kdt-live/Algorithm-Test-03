t = int(input())

for i in range(1, t+1):
    n, k = map(int, input().split())
    puzzle = []

    for j in range(n):
        puzzle.append(list(map(int, input().split())))
        
    word = []
    cnt = 0
    for a in range(n):
        for b in range(n):
            if puzzle[a][b] == 0:
                if cnt not in [0, 1]:
                    word.append(cnt)
                    cnt = 0
                else:
                    cnt = 0
            else:
                if b != n-1:# 마지막이 아닐때
                    cnt += 1  
                else:#마지막일때
                    cnt +=1
                    if cnt not in [0, 1]:
                        word.append(cnt)
                        cnt = 0
                    else:
                        cnt =0

    for a in range(n):
        for b in range(n):
            if puzzle[b][a] == 0:
                if cnt not in [0, 1]:
                    word.append(cnt)
                    cnt = 0
                else:
                    cnt = 0
            else:
                if b != n-1:# 마지막이 아닐때
                    cnt += 1  
                else:#마지막일때
                    cnt +=1
                    if cnt not in [0, 1]:
                        word.append(cnt)
                        cnt = 0
                    else:
                        cnt =0

    print(word)

                


