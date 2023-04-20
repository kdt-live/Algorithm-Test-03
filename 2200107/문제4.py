# swea 1979번 어디에 단어가 들어갈 수 있을까 D2
from pprint import pprint
T=int(input())
for tc in range(T):
    N,K=map(int,input().split())
    li=[list(map(int,input().split())) for _ in range(N)]
    transform_li=[([0]*N) for _ in range(N)]
    for p in range(N):
        for q in range(N):
            transform_li[p][q]=li[q][p]
    # pprint(transform_li)
    cnt=0
#     # index 범위 잡는데에서 실수함.
#     # i for 구문에서는 range를 N-K로 했었는데, 아까 파리 퇴치 때문에 헷갈림.
#     # 행 우선순회 행렬과 열 우선순회 행렬 두 개를 만들었으므로
#     # 각각에 대한 행 우선순회 행렬만 만들어도 됨.
#     # 따라서 i는 range 범위 제한 없이 N에서 stop하면 됨.
    for i in range(N):
#         # j에서 실수했는데, j의 range범위가 N-K라고 생각했음.
#         # 일견 맞아뵈지만, 사실은 N이 5 K가 3이라고 하면
#         # N=2가 돼버리고, 실제로 실행은 j=0, j=1만 실행하게 됨.
#         # 따라서 (N-K)+1로 해야 맞음. 왜냐면, stop number를 쓰는 곳이므로.
        
#         # 아 또 실수했는데... 1 1 1 1 등 3개 이상 되는 거는 카운트 하면 안됨.
#         # 이 추가 조건 어떻게 설정하지
#         # 추가 조건 설정 방법 : 행 인덱스 -1, +1 했을 때 K보다 큰 수 나오면
#         # 패스
#         # 인덱스 에러 발생하므로
#         # try : except : 사용
        for j in range(N-K+1):
                if sum(li[i][j:j+K])==K:
                    # print(i,j,K)
                    try:
                        if sum(li[i][j:j+K+1])>K:
                            pass
                        elif sum(li[i][j-1:j+K])>K:
                            pass
                        else:
                            # print(f'i={i},j={j},K={K}')
                            # print('li')
                            cnt+=1
                    except:
                        cnt+=1
                if sum(transform_li[i][j:j+K])==K:
                    try:
                        if sum(transform_li[i][j:j+K+1])>K:
                            pass
                        elif sum(transform_li[i][j-1:j+K])>K:
                            pass
                        else:
                            # print(f'i={i},j={j},K={K}')
                            # print('transform_li')
                            cnt+=1
                    except:
                        cnt+=1
    print(f'#{tc+1} {cnt}')


# from pprint import pprint
# T=int(input())
# for tc in range(T):
#     N,K=map(int,input().split())
#     li=[list(map(int,input().split())) for _ in range(N)]

#     transform_li=[([0]*N) for _ in range(N)]
#     # pprint(li)
#     # pprint(transform_li)
#     for p in range(N):
#         for q in range(N):
#             transform_li[p][q]=li[q][p]
#     # pprint(li)
#     pprint(transform_li)
#     cnt=0
#     # index 범위 잡는데에서 실수함.
#     # i for 구문에서는 range를 N-K로 했었는데, 아까 파리 퇴치 때문에 헷갈림.
#     # 행 우선순회 행렬과 열 우선순회 행렬 두 개를 만들었으므로
#     # 각각에 대한 행 우선순회 행렬만 만들어도 됨.
#     # 따라서 i는 range 범위 제한 없이 N에서 stop하면 됨.
#     for i in range(N):
#         # j에서 실수했는데, j의 range범위가 N-K라고 생각했음.
#         # 일견 맞아뵈지만, 사실은 N이 5 K가 3이라고 하면
#         # N=2가 돼버리고, 실제로 실행은 j=0, j=1만 실행하게 됨.
#         # 따라서 (N-K)+1로 해야 맞음. 왜냐면, stop number를 쓰는 곳이므로.
        
#         # 아 또 실수했는데... 1 1 1 1 등 3개 이상 되는 거는 카운트 하면 안됨.
#         # 이 추가 조건 어떻게 설정하지
#         # 추가 조건 설정 방법 : 행 인덱스 -1, +1 했을 때 K보다 큰 수 나오면
#         # 패스
#         # 인덱스 에러 발생하므로
#         # try : except : 사용
#         for j in range(N-K+1):
#                 if sum(li[i][j:j+K])==K:
#                     # print(i,j,K)
#                     try:
#                         if sum(li[i][j:j+K+1])>K:
#                             pass
#                         elif sum(li[i][j-1:j+K])>K:
#                             pass
#                         else:
#                             # print(f'i={i},j={j},K={K}')
#                             # print('li')
#                             cnt+=1
#                     except:
#                         cnt+=1
#                 if sum(transform_li[i][j:j+K])==K:
#                     try:
#                         if sum(transform_li[i][j:j+K+1])>K:
#                             pass
#                         elif sum(transform_li[i][j-1:j+K])>K:
#                             pass
#                         else:
#                             # print(f'i={i},j={j},K={K}')
#                             # print('transform_li')
#                             cnt+=1
#                     except:
#                         cnt+=1
#     print(f'#{tc+1} {cnt}')