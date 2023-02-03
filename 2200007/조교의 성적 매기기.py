T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for t in range (1, T+1) :
    N, K = map(int,input().split())
    data = []
    for n in range(N) :
        mid, final, hw = map(int, input().split())
        sum_value = (mid * 0.35) + (final * 0.45) + (hw * 0.2)
        data.append(sum_value)

    k_score = data[K-1]
    data.sort(reverse=True)

    value = N // 10
    result = data.index(k_score) // value

    print(f"#{t} {grade[result]}")