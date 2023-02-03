import sys
sys.stdin = open('2200053/input.txt')

T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for t in range(1, T+1):
    N, K = map(int, input().split())
    result = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        cnt = (a * 0.35) + (b * 0.45) + (c * 0.2)
        result.append(cnt)
        #print(cnt)
    #print(result)

    # K번째 학생
    K_student = result[K - 1]
    #print(K_student)
    result.sort(reverse=True)
    #print(result)

    score = (result.index(K_student) // (N // 10))
    #print(score)
    print(f'#{t} {grade[score]}')