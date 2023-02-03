# 민석이의 과제 체크하기 

T = int(input())

for t in range(1,T+1):
    # 수강생수 , 과제 제출한 사람 
    a, b = list(map(int,input().split()))
    # 제출 사람 번호 
    c = list(map(int,input().split()))
    d = []
    for i in range(1,a+1):
        if i not in c :
            d.append(i)
    print(f'#{t}', *d)