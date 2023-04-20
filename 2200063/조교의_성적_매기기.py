T = int(input())
score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for t in range(T):
    N, K = map(int, input().split())
    dict_ = {}
    for n in range(1, N+1):
        A, B, C = map(int, input().split())
        dict_[n] = (A*0.35) + (B*0.45) + (C*0.2)

    X = dict_[K]
    dict_ = sorted(dict_.values(), reverse=True)

    N2 = int(N/10)
    result = 0

    while len(dict_):        
        for i in range(N2):            
            if X == dict_[i]:
                print(f'#{t+1} {score[result]}')
                X = 0
                break                            
        else:
            for j in range(N2):
                dict_.pop(0)
            result += 1

        if X == 0:
            break