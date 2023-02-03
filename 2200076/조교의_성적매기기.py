T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for t in range(T):
    n, k = map(int, input().split())
    score = []
    # 나중에 k의 점수 알아볼 수 있도록 변수에 담아놓기
    k_score = 0
    for i in range(n):
        a, b, c = map(int, input().split())
        score.append((a*35+b*45+c*20)/100)
        if i+1 == k:
            k_score = (a*35+b*45+c*20)/100
    
    score.sort(reverse=True)
    k_rank = score.index(k_score)
    # 내림차순으로 정렬 후 k의 등수를 n//10으로 나눈 몫이 k의 등급 index
    print(f'#{t+1} {grade[k_rank//(n//10)]}')
