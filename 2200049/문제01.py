for i in range(10):
  l = int(input())
  str = input()
  arr1 = [] #()
  arr2 = [] #[]
  arr3 = [] #{}
  arr4 = [] #<>
  valid = True
  for s in str:
    if s=='(':
      arr1.append(s)
    elif s=='[':
      arr2.append(s)
    elif s=='{':
      arr3.append(s)
    elif s=='<':
      arr4.append(s)
    elif s==')':
      if arr1:
        arr1.pop()
      else:
        valid=False
    elif s==']':
      if arr2:
        arr2.pop()
      else:
        valid=False
    elif s=='}':
      if arr3:
        arr3.pop()
      else:
        valid=False
    elif s=='>':
      if arr4:
        arr4.pop()
      else:
        valid=False
  if not valid:
    print(f"#{i+1}",0)
  else:
    if len(arr1)==0 and len(arr2)==0 and len(arr3)==0 and len(arr4)==0:
      print(f"#{i+1}",1)
    else:
      print(f"#{i+1}",0)
