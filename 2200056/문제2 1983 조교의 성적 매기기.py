T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split()) # N명의 학생수 K번째 학생
    total_list = []
    abcd = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D"] # 학점 리스트
    score = [] # 새로운 학점을 만들기 위한 리스트
    N_10  = N // 10
    # 학점 리스트를 만들기 위한 for문
    for ab in abcd:
        for _ in range(N_10): # N/10명에게 동일한 평점을 주기 위해 N/10만큼 객체들 리스트에 추가
            score.append(ab)

    for _ in range(N): # 학생 점수 리스트 만들기
        a, b, c = map(int, input().split())
        total = a*0.35 + b*0.45 + c*0.2
        total_list.append(total)
    
    K_score = total_list[K-1] # K번째 학생 점수 구하기
    new_total_list = sorted(total_list, reverse=True) # 내림차순으로 정렬
    
    # 정답 딕셔너리를 만들기 학생 점수를 key로 학점을 value로...
    result_dict = {}
    for n in range(N):
        result_dict[new_total_list[n]] = score[n]
    
    print(f"#{t} {result_dict[K_score]}")

# 여기에서 가장 시간을 많이 쓴 곳은 어떻게 하면 학점을 만들 수 있을까? 였다
# 처음 접근은 학점리스트에 *N//10을 해줬지만 그렇게 되면 aabbcc가 아닌 abcabc가 돼서 실패
# 리스트*N//10 후 정렬하면 되지 않을까? 했지만 +-0순으로 정렬돼서 이것도 실패
# 결국은 반복문을 돌려서 N//10만큼 반복해서 추가해주는 방법을 썼다.
# 마지막에 굳이 딕셔너리를 쓰지 않아도 될 것 같은 생각이 들지만 그래도 직관적으로 모든 점수와 학점을 볼 수 있어 만족한다.