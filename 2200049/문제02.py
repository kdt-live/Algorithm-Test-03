def stop(arr):
  for a in arr:
    if a<=0:
      return True
  return False

for _ in range(10):
  index = int(input())
  arr = list(map(int,input().split()))

  b = False
  while True:
    if b:
      break
    for i in range(1,6):
      a1 = arr[0]
      arr.pop(0)
      arr.append(a1-i)
      if stop(arr):
        b = True
        break
      #print("arr",*arr)

  for idx,a in enumerate(arr):
    if a<=0:
      arr[idx]=0
  print(f"#{index}",*arr)