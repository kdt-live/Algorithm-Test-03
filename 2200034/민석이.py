#민석이는 교수가 됨 처음으로 맡은 수강생 N명
#과제를 냈고 제출한 사람의 목록을 받았다
#수강생들은 1 ~ N까지의 번호가 매겨져있고 어떤 번호의 사람이 제출했는지 대한 목록을 받음
#과제를 제출하지 않은 사람의 번호를 오름차순 출력

T = int(input())
lists = []
A = []
for i in range(1,T + 1):
    N,M = map(int,input().split())
    K = list(map(int,input().split()))

    for t in range(1,N + 1):
        lists.append(t)
    
    for re in range(len(lists)):
        if lists[re] not in K:
           A.append(lists[re])
    print(f'#{i}',end=" ")
    print(*A)
    A = []
    lists = []




