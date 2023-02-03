# 5431
T = int(input())

for t in range(1, T+1):

    tot, good = list(map(int, input().split()))
    good_students = list(map(int, input().split()))
    bad_students = []

    for a in range(1, tot+1):
        if a not in good_students:
            bad_students.append(a)

    print(f'#{t}', *bad_students)

# 2001 
T = int(input())

for t in range(1, T+1):
    n, m = map(int, input().split())
    nxn = [list(map(int, input().split())) for num in range(n)]
    max_flies = []

    for another in range(n -m +1):
        for num in range(n -m + 1):
            for i in range(m):
                for x in range(m):
                    max_flies.append(nxn[i + num][x + another])

    kills = 0
    kills_record = []

    for count in range(1, len(max_flies)+1):
        if count % (m*m) == 0:
            kills += max_flies[count -1]
            kills_record.append(kills)
            kills = 0
        else:
            kills += max_flies[count -1]

    kills_record = sorted(kills_record)

    print(f'#{t}', kills_record[-1], sep=' ')

# 1983

T = int(input())

for t in range(1, T+1):
    n, k = map(int, input().split())
    scores = [list(map(int, input().split())) for _ in range(n)]
    total_scores = []

    for x in scores:
        total_scores.append(0.35 * x[0] + 0.45 * x[1] + 0.2 * x[2])
    
    k = total_scores[k -1]

    total_scores = sorted(total_scores, reverse=True)

    index_in = total_scores.index(k)

    if (index_in + 1) / (n//10) <= 1:
        print(f'#{t} A+')
    elif (index_in + 1) / (n//10) <= 2:
        print(f'#{t} A0')
    elif (index_in + 1) / (n//10) <= 3:
        print(f'#{t} A-')
    elif (index_in + 1) / (n//10) <= 4:
        print(f'#{t} B+')
    elif (index_in + 1) / (n//10) <= 5:
        print(f'#{t} B0')
    elif (index_in + 1) / (n//10) <= 6:
        print(f'#{t} B-')
    elif (index_in + 1) / (n//10) <= 7:
        print(f'#{t} C+')
    elif (index_in + 1) / (n//10) <= 8:
        print(f'#{t} C0')
    elif (index_in + 1) / (n//10) <= 9:
        print(f'#{t} C-')
    elif (index_in + 1) / (n//10) <= 10:
        print(f'#{t} D0')

# 1979

T = int(input())

for t in range(1, T+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[i][j] == 1:
                cnt+=1
            if arr[i][j] == 0 or j == n-1:
                if cnt == k:
                    result += 1
                cnt = 0
        for j in range(n):
            if arr[j][i] == 1:
                cnt+=1
            if arr[j][i] == 0 or j == n-1:
                if cnt == k:
                    result += 1
                cnt = 0

    print(f'#{t} {result}')
                    





            

    
            
    

    