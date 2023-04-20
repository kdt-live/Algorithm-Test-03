# 조교의 성적 매기기

T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    total = []
    K_index = 0
    percent = N // 10

    s = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    for i in range(N):
        scores = list(map(int, input().split()))
        total.append(((scores[0] * 0.35) + (scores[1] * 0.45) + (scores[2] * 0.2)))

    K_index = total[K-1]
    sorted_list = sorted(total, reverse=True)

    ans = sorted_list.index(K_index) // percent
    print(s[ans])










