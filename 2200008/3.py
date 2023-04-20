# 조교의 성적 매기기
def total(score):
    nsco = 0.35*score[0] + 0.45*score[1] + 0.2*score[2]
    return nsco

def grade(inde):
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    inde = inde // (n//10)
    gra = grades[inde]
    return gra

for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    sco = {i: list(map(int, input().split())) for i in range(1, n+1)}

    for key in sco:
        sco[key] = total(sco[key])
    
    sort_sco = sorted(sco, key= lambda x: sco[x], reverse = True)

    print(f'#{t} {grade(sort_sco.index(k))}')