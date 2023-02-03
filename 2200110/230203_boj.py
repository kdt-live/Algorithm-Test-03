# 5431 민석이의 과제 체크하기
from collections import deque
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    not_s = []
    success = list(map(int, input().split()))

    for i in range(1, N+1):
        if i not in success:
            not_s.append(i)

    print(f'#{t}', *sorted(not_s))


# 2001 파리 퇴치

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    matrix = []
    cnt = 0
    max_cnt = 0
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    for m in range(N-M+1):
        for k in range(N-M+1):
            for i in range(M):
                for j in range(M):
                    cnt += matrix[m+i][k+j]

            if max_cnt < cnt:
                max_cnt = cnt

            cnt = 0

    print(f'#{t} {max_cnt}')
# matrix[m][k] matrix[m][k+1] matrix[m][k+2] ... matrix[m][k+M-1]
# matrix[m+1][k] matrix[m+1][k+1] ... matrix[m+1][k+M-1]
# ...
# matrix[m+M-1][k]

# 조교의 성적 매기기
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    score = {}
    for k in range(N):
        mid, fin, ass = map(int, input().split())
        score[k] = mid*0.35 + fin*0.45 + ass*0.2

    print(score)
    new_score = sorted(score.items(), key=lambda x: x[1])
    print(new_score)

    for i in range(len(new_score)):
        if new_score[i][0] == K-1:
            if i >= N * 0.9:
                print(f'#{t} A+')
            elif i >= N * 0.8:
                print(f'#{t} A0')
            elif i >= N * 0.7:
                print(f'#{t} A-')
            elif i >= N * 0.6:
                print(f'#{t} B+')
            elif i >= N * 0.5:
                print(f'#{t} B0')
            elif i >= N * 0.4:
                print(f'#{t} B-')
            elif i >= N * 0.3:
                print(f'#{t} C+')
            elif i >= N * 0.2:
                print(f'#{t} C0')
            elif i >= N * 0.1:
                print(f'#{t} C-')
            else:
                print(f'#{t} D0')


# 어디에 단어가 ~
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = []
    cnt = 0
    result = 0
    for _ in range(N):
        puzzle.append(list(map(int, input().split())))

    for n in range(N):
        for m in range(N):
            if puzzle[n][m] == 1:
                cnt += 1

            elif puzzle[n][m] == 0:
                if cnt == K:
                    result += 1
                cnt = 0

        if cnt == K:
            result += 1
            cnt = 0

        cnt = 0

    for n in range(N):
        for m in range(N):
            if puzzle[m][n] == 1:
                cnt += 1
            elif puzzle[m][n] == 0:
                if cnt == K:
                    result += 1
                cnt = 0

        if cnt == K:
            result += 1
            cnt = 0

        cnt = 0

    print(f'#{t} {result}')


# 1225 [S/W 문제해결 기본] 7일차 - 암호생성기

for i in range(10):
    T = int(input())
    nums = deque(map(int, input().split()))
    i = 1

    while True:
        if nums[0]-i > 0:
            nums.append(nums.popleft()-i)
        i += 1

        if i == 6:
            i = 1

        if nums[0]-i <= 0:
            nums.popleft()
            nums.append(0)
            print(f'#{T}', *nums)
            break


# 아래는 반복 없는 버전

T = int(input())
nums = deque(map(int, input().split()))
i = 1

while True:
    if nums[0]-i > 0:
        nums.append(nums.popleft()-i)

        i += 1

    if i == 6:
        i = 1

    if nums[0]-i <= 0:
        nums.popleft()
        nums.append(0)
        print(f'#{T}', *nums)
        break


# [S/W 문제해결 기본] 4일차 - 괄호 짝짓기 D4

for t in range(1, 11):
    r = int(input())
    R = input()
    s = 0
    m = 0
    l = 0
    el = 0

    for i in range(r):
        if R[i] == '(':
            s += 1

        if R[i] == ')':
            s -= 1

        if R[i] == '[':
            m += 1

        if R[i] == ']':
            m -= 1

        if R[i] == '{':
            l += 1

        if R[i] == '}':
            l -= 1

        if R[i] == '<':
            el += 1

        if R[i] == '>':
            el -= 1

        if s < 0 or m < 0 or l < 0 or el < 0:
            print(f'#{t} 0')
            break

    if s == 0 and m == 0 and l == 0 and el == 0:
        print(f'#{t} 1')

    elif s > 0 or m > 0 or l > 0 or el > 0:
        print(f'#{t} 0')

    (({{)})}  X
    ({} < [] > )  O
    ({ < } > )    X
