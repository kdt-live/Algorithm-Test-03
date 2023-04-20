'''
1
6 3
29 21 26 9 5 8
21 19 8 0 21 19
9 24 2 11 4 24
19 29 1 0 21 19
10 29 6 18 4 3
29 11 15 3 3 29
'''
t = int(input())
for case in range(1,t+1):
  n,m = map(int, input().split())
  matrix = [list(map(int, input().split())) for _ in range(n)]

  dx = [] # [0, 0, 0, 1, 1, 1, 2, 2, 2]  
  dy = [] # [0, 1, 2, 0, 1, 2, 0, 1, 2]  

  for x in range(m):
    for y in range(m):
      dx.append(x)
      dy.append(y)

  max_sum = 0
  for i in range(n):
    for j in range(n):
      sum = 0
      for k in range(m*m):
        nx = i + dx[k]
        ny = j + dy[k]

        if 0 <= nx < n and 0<= ny < n:
          sum += (matrix[nx][ny])
      if max_sum < sum:
          max_sum = sum
  print(f'#{case}',max_sum)