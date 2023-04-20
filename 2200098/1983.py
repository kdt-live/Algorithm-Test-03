import sys
sys.stdin = open('1983.txt', 'r')

T = int(sys.stdin.readline())
scores = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for t in range(1, T+1):
    N, K = map(int, sys.stdin.readline().split())
    split_point = N // 10
    students = []
    for n in range(1, N+1):
        mid, final, task = map(int, sys.stdin.readline().split())
        total = (mid * 0.35) + (final * 0.45) + (task * 0.2)
        students.append([total, n])
    students.sort(reverse = True)
    ranking = 0
    for i in range(len(students)):
        if students[i][1] == K:
            ranking = i
    k_score = scores[ranking//split_point]
    print('#' + str(t), k_score)