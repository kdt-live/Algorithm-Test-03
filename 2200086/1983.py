# 조교의 성적 매기기

ABCD = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
T = int(input())
for t in range(1, T + 1):
    N, K = list(map(int, input().split()))
    
    students = N//10
    score = []
    for j in range(1, N + 1):
        a, b, c = list(map(int, input().split()))
        score.append((a*0.35) + (b*0.45) + (c*0.2))
    
    K_score = score[K-1]

    score2 = sorted(score, reverse= True)
    
    K_rank = score2.index(K_score) // students
    print(f'#{t} {ABCD[K_rank]}') 





# 딕셔너리 실패
    # students = K/10
    # score = {}
    # for j in range(1, N + 1):
    #     a, b, c = list(map(int, input().split()))
    #     score[j] = (a*0.35) + (b*0.45) + (c*0.2)
    
    # score2 = sorted(score.items(), key= lambda x: x[1], reverse= True)
    # # print(score2)
    # for w in range(1, K + 1):
    #     for k in ABCD:
    #         print(k)
