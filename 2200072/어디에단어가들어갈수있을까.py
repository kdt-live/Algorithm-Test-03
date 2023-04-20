'''
1
5 3
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1
'''
def puzzle_count(matrix, target_num) :
  total_sum_list = []
  for row in matrix:
      total_sum = 0
      for i in range(n):
        if row[i] == 1:
          total_sum += 1
        else:
          total_sum_list.append(total_sum)
          total_sum = 0

      total_sum_list.append(total_sum)
  return total_sum_list.count(target_num)

t = int(input())
for case in range(1,t+1):
  n,k = map(int, input().split())
  matrix = [list(map(int, input().split())) for _ in range(n)]
  result = puzzle_count(matrix,k) + puzzle_count(list(zip(*matrix[::-1])),k)

  print(f'#{case}', result)