for index in range(int(input())):
  N,M = map(int,input().split())
  arr = [list(map(int,input().split())) for _ in range(N)]
  maxn = 0
  for i in range(N):
    for j in range(N):
      tmp = 0
      if i+M<=N and j+M<=N:
        for k in range(M):
          for d in range(M):
            tmp+=arr[i+k][j+d]
            #print(arr[i+k][j+d],"를 더함")
      if tmp>maxn:
        maxn=tmp
      #print("--\n")
  print(f"#{index+1}",maxn)