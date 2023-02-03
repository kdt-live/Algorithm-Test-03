for idx in range(int(input())):
  N,K = map(int,input().split())
  arr=[]
  for _ in range(N):
    arr.append(input().split())
  cnt=0
  for i in range(N):
    tmp=""
    for s in arr[i]:
      tmp+=s
    for a in tmp.split('0'):
      if len(a)==K:
        cnt+=1
  for i in range(N):
    tmp=""
    for j in range(N):
      tmp+=arr[j][i]
    for a in tmp.split('0'):
      if len(a)==K:
        cnt+=1
  print(f"#{idx+1}",cnt)
