T = int(input())

for t in range(1, T+1) :
    n, s = map(int, input().split())

    matrix = [[0]*n for _ in range(5)]
    # print(matrix) 
    for i in range(5) :
        li = list(input().split())
        