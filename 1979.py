T = int(input())

for t in range(1, T+1):
    a, b = map(int, input().split())
    puzzle = []

    for _ in range(a):
        puzzle.append(list(map(int, input().split())))

    result = []


    for i in range(len(puzzle)):
        cnt = 0
        for j in range(len(puzzle[i])):
            
            if puzzle[i][j]:
                cnt +=1
            
            else:
                result.append(cnt)
                cnt = 0
        
        result.append(cnt)

    
    for j in range(len(puzzle[0])):
        cnt = 0
        for i in range(len(puzzle)):
            if puzzle[i][j]:
                cnt += 1
            else:
                result.append(cnt)
                cnt = 0
        result.append(cnt)

    
    ans = 0
    for num in result:
        if num == b:
            ans += 1

    print('#{} {}'.format(t, ans))