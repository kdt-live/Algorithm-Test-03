T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split()) # N은 단어퍼즐 크기 K는 단어 길이
    matrix = [] 
    total = 0
    for _ in range(N): # 이중리스트 만들기
        num_list = list(map(int, input().split()))
        matrix.append(num_list)

    for num in matrix: # 이중리스트 돌기 시작!
        cnt = 0 # 카운팅 변수 만들기 & 초기화
        result = 0 # result변수 만들기 & 초기화
        for n in range(N): # 이중리스트 안에 리스트 돌기
            if num[n] == 1:   # 1이 나오면 카운팅 해주기     
                cnt += 1     
                if cnt == K: # 카운팅이 k가 되면
                    result = 1 # result는 1해주기
                elif cnt >= K: # 대신 k보다 커지면
                    result = 0 # 다시 result 0으로 초기화

            elif num[n] == 0:    # 0이면 두가지로 나누기
                if result == 1: # 그 전에 1이 k번 나와서 result가 1이면
                    total += result # 토탈 값에 +result 해주고 변수들 초기화
                    result = 0
                    cnt = 0
                else:  # K번 나오지 않았으면 카운팅 변수 초기화
                    cnt = 0
        total += result # 다음 리스트 돌기 전에 토탈값에 result 저장해주기
    
    # 세로도 보기 위해 행열 반대인 이중 리스트 만들기
    new_matrix = [[0]*N for _ in range(N)]

    for i in range(N): # 빈 리스트에 행열반대인 값 넣기 
            for j in range(N):
                new_matrix[i][j] = matrix[j][i]
    # 위와 같은 방법
    for num2 in new_matrix:
        cnt2 = 0
        result = 0
        for n2 in range(N):
            if num2[n2] == 1:
                cnt2 += 1 
                if cnt2 == K:
                    result = 1
                elif cnt2 > K:
                    result = 0

            elif num2[n2] == 0:
                if result == 1:
                    total += result
                    result = 0
                    cnt2 = 0
                else:
                    cnt2 = 0
        total += result
    print(f"#{t} {total}")      
# 이 문제에서 가장 어려웠던 점은 가정문을 이렇게 많이 써도 되나 싶을 정도로 써서...
# 변수 초기화나, 누적값 저장해주는걸 어느 지점에서 하는지 헷갈린게 컸다.
# 제대로 된 위치에 넣지 않으면 되면 자꾸 출력값이 0이 떠서 이곳 저곳 변수 초기화 시켰다가 멘붕와서 시간을 낭비한게 크다
# 그래서 다시 차근차근 중간 중간 프린트 하면서 어느곳에 넣어야 하는지,
# 또 어느 예외에서 잘 못된건지 확인하니까 풀 수 있었다.
# 이 문제는 다 풀고 나서도 식이 지저분해서 만족스럽지는 못하다.
# 이중 리스트에다, 행열 반대로도 봐야하니 코드 길이가 너무 길어졌는데, 
# 좀 더 깔끔하게 작성 할 수 있는 방법이 분명 있을거라 확인해봐야 할 것 같다.
# 이렇게 무자비하게 가정문을 써도 되는 것인지 의문이 든다.