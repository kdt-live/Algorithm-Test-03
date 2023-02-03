#5431. 민석이의 과제 체크하기
T = int(input()) # 테스트 케이스 수
for i in range(T):
    li = []
    a, = map(int, input().split())
    c = list(map(int, input().split()))
    for j in range(1, a+1):
        if j not in c:
            li.append(j)
    print(f'#{i+1}', *li)

#파리 퇴치
T = int(input()) # 테스트 케이스 수
for t in range(T):
    N,  M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []

    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            for k in range(M):
                for l in range(M):
                    sum += arr[i+k][j+l]
            result.append(sum)

    print(f'#{t+1}', max(result))




#1983. 조교의 성적 매기기
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
T = int(input()) # 테스트 케이스 수
for i in range(T):
    a, b = map(int, input().split())
    li = []
    for z in range(1, a+1):
        c, d, e = list(map(int, input().split()))
        g = c * 0.35 + d * 0.45 + e * 0.2
        li.append((g, z))
    
    li.sort(reverse=True)

    for j in range(a):
        if li[j][1] == b:
            print(f'#{i+1}', grades[(j // (a//10)) % 10])
            break

#어디에 단어가 들어갈 수 있을까
T = int(input()) # 테스트 케이스 수
for t in range(T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            if arr[i][j] == 0 or j == N - 1:
                if cnt == K:
                    result += 1
                cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            if arr[j][i] == 0 or j == N - 1:
                if cnt == K:
                    result += 1
                cnt = 0
    print(f'#{t+1}', result)

#1225. [S/W 문제해결 기본] 7일차 - 암호생성기
for t in range(10):
    T = int(input())
    num = list(map(int, input().split()))
    while num[-1] != 0:
        for i in range(5):
            num.append(num.pop(0)-(i+1))
            if num[-1] <= 0:
                num[-1] = 0
                break
    print(f'#{t+1}', *num)



#[S/W 문제해결 기본] 4일차 - 괄호 짝짓기
for t in range(1, 11):
    N = int(input())
    arr = input()
    li = []
    result = 1

    for i in range(N):
        if arr[i] == '(' or arr[i] == '{' or arr[i] == '[' or arr[i] == '<':
            li.append(arr[i])
        
        if arr[i] == ')':
            if len(li) > 0 and li.pop() != '(':
                result = 0
                break
        if arr[i] == '}':
            if len(li) > 0 and li.pop() != '{':
                result = 0
                break
        if arr[i] == ']':
            if len(li) > 0 and li.pop() != '[':
                result = 0
                break
        if arr[i] == '>':
            if len(li) > 0 and li.pop() != '<':
                result = 0
                break

    print(f'#{t}', result)