import sys
sys.stdin = open('1979.txt', 'r')
T = int(sys.stdin.readline())
for t in range(1, T+1):
    N, K = map(int, sys.stdin.readline().split())
    puzzle = []
    for _ in range(N):
        line = list(map(int, sys.stdin.readline().split()))
        puzzle.append(line)
    readR = []
    for r1 in range(N):
        cnt = 0
        for c1 in range(N):
            if puzzle[r1][c1] == 1:
                cnt += 1
            elif cnt != 0:
                readR.append(cnt)
                cnt = 0
        if cnt > 0:
            readR.append(cnt)
    readC = []
    for c2 in range(N):
        cnt = 0
        for r2 in range(N):
            if puzzle[r2][c2] == 1:
                cnt += 1
            elif cnt != 0:
                readC.append(cnt)
                cnt = 0
        if cnt > 0:
            readC.append(cnt)
    answer = readR.count(K) + readC.count(K)
    print('#' + str(t), answer)