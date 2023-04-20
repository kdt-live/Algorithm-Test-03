T = int(input())
for t in range(1, T+1):
    students = set([]) # 차집합 이용하기 위해서 set사용
    N, K = map(int, input().split())
    for i in range(1, N+1):
        students.add(i) # 수강생 번호 담기
    num_list = set(map(int, input().split())) #과제 제출자 set으로 받기
    print(f"#{t}", end=" ")
    print(*(students - num_list)) # set은 자동정렬로 오름차순으로 나옴