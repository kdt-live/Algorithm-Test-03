T = int(input())
for t in range(1, T+1):
    N, K =  map(int, input().split())
    number = map(int, input().split())
    lst = []
    lit = []
    for i in range(1, N+1): # 차집합에 사용할 학생수에 맞는 리스트 추가 및 생성
        lst.append(i)

    for j in number: # 과제 제출한 학생 번호 리스트에 추가
        lit.append(j)

    set1 = set(lst)
    set2 = set(lit)
    set3 = (set1 - set2) # 차집합으로 빼면 과제 미제출자 번호만 나온다
    
    print(f'#{t}', *set3) # set3으로 출력하면 {}가 있으므로 *으로 괄호 제거