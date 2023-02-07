# 어디에 단어가 들어갈 수 있을까

t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    puzzle = [[0 for j in range(n)]for l in range(n)]
    result = 0

    for j in range(n):
        puzzle[j] = list(map(int, input().split()))
        chk = 0

        for l in range(n):
            if puzzle[j][l]:
                chk += 1
                if (l == (n - 1)) and (chk == k):
                    result += 1
            else:
                if chk == k:
                    result += 1
                chk = 0
    
    for j in range(n):
        chk = 0
        for l in range(n):
            if puzzle[l][j]:
                chk += 1
                if (l == (n - 1)) and (chk == k):
                    result += 1
            else:
                if chk == k:
                    result += 1
                chk = 0

    print(f'#{i + 1} {result}')