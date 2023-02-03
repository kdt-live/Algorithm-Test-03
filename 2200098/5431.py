T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    students = [0 for _ in range(N)]
    submits = [*map(int, input().split())]
    for num in submits:
        students[num-1] = 1
    answers = []
    for i in range(len(students)):
        if students[i] == 0:
            answers.append(i+1)
    print('#'+ str(t + 1), *answers)