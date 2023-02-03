
t = int(input())

for i in range(1, t + 1) :
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    result = []

    for j in range(1, n + 1) :
        if j not in numbers :
            result.append(j)
            
             
    print(f'#{i}',*result)

