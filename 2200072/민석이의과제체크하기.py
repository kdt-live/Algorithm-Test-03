
t = int(input())
for i in range(t):
  n,_ = map(int, input().split())
  numbers = {num for num in range(1,n+1)}
  submit_number = map(int, input().split())
  not_submit_number = sorted(list(numbers - set(submit_number)))
  print(f'#{i+1}',*not_submit_number)

