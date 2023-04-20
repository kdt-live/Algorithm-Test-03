#어디에 단어가 들어갈 수 있을까
from pprint import pprint 

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())# 길이와 , 단어의 길이
    
    puzzle = []

    for _ in range(N):
        nums = list(map(int, input().split()))
        puzzle.append(nums)
        answer = 0

    for i in range(N): #열순회
        cnt = 0
        for j in range(N):
            #조건1 1은 연속해서 3개여야함 그 다음에도 1이 나오면 안됨
            if puzzle[i][j] == 0 and cnt == K:
                answer += 1
                cnt = 0
            elif puzzle[i][j] == 0:
                cnt = 0
            elif puzzle[i][j] == 1:
                cnt += 1
        else:
            if cnt == K:
                answer += 1
    
    for i in range(N): #행순회
        cnt = 0
        for j in range(N):
            #조건1 1은 연속해서 3개여야함 그 다음에도 1이 나오면 안됨
            if puzzle[j][i] == 0 and cnt == K:
                answer += 1
                cnt = 0
            elif puzzle[j][i] == 0:
                cnt = 0
            elif puzzle[j][i] == 1:
                cnt += 1
        else:
            if cnt == K:
                answer += 1
    print(f'#{test_case}',answer)