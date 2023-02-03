T = int(input())

grades = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

for test_case in range(1,T+1):
    a, b = map(int,input().split())

    list = []

    for i in range(a):
        mid, final, work = map(int,input().split())
        total = (mid * 0.35) + (final * 0.45) + (work * 0.2)
        list.append(total)

    k_score = list[b-1]

    list.sort(reverse=True)

    div = a // 10
    final_k_score = list.index(k_score) // div

    print('#{} {}'.format(test_case, grades[final_k_score]))