import sys
sys.stdin = open('2001.txt', 'r')

T = int(sys.stdin.readline())
for t in range(1, T+1):
    N, M = map(int, sys.stdin.readline().split())
    matrix = []
    for _ in range(N):
        matrix.append([*map(int, sys.stdin.readline().split())])
    answers = []
    for st_r in range(N-M+1):
        for st_c in range(N-M+1):
            cnt = 0
            for num in range(M):
                cnt += sum(matrix[st_r+num][st_c : st_c+M])
            answers.append(cnt)
    answer = max(answers)
    print('#' + str(t), answer)