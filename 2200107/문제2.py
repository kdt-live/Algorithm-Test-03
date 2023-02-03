# swea 2001번 파리 퇴치 D2
# from pprint import pprint
T=int(input())
for tc in range(T):
    N,M=map(int,input().split())
    mat=[list(map(int,input().split())) for i in range(N)]
    # pprint(mat)
    total_li=[[] for _ in range(N**2)]
    k=0
    # i는 mat[][]에서 행을 의미, j는 열을 의미.
    # 그런데, input으로 주어지는 M*M 파리채 크기에 따라 j와 i의 크기가 변함
    # 행 우선순회를 통하여 구함. 따라서, [j:j+M] 인덱싱으로 행 우선 순회하고
    # 열도 M*M이므로 M만큼 구해야 함.
    # 근데, 인덱싱을 써보니 [i:i+M][j:j+M] 이런 형태는 안됨. 쩝.
    # 그래서 생각을 함. i에다가 M만큼 하려면 어떻게 해야 하나
    # p를 인자로 하는 for구문을 하나 더 만들어서 start=0,stop=M의
    # 범위에서 p가 굴러가게 짬.
    # 이를 통해, 행 우선 순회 후 p만큼 열 기준으로 순회하게 만들고,
    # i for 구문에 total 더해봤는데, 그럼 값이 안 맞음.
    # 왜냐면, i를 기준으로 잡으면 [j:j+M]으로 행 우선순회 기준을
    # 잡은 게 의미가 없어짐.
    # 행 우선 순회 기준으로, i는 열도 더하는 것이므로
    # j가 기준이 되어야 값이 나옴.
    for i in range(N):
        for j in range(N):
            total=0
            for p in range(M):
                # print(f'mat출력 {mat[i:i+M][j:j+M]}')
                try:
                    total+=sum(mat[i+p][j:j+M])
                    print(f'i={i},j={j},p={p}')
                    # print(f'mat출력 {mat[i+p][j:j+M]}')
                    print("total_li")
                    print(total_li)
                except:
                    pass
            total_li[k]=total
            k+=1
    print(f'#{tc+1} {max(total_li)}')
    print(max(total_li))
    # for i in range(N):
        # for j in range(M):